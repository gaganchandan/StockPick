import config
import argparse
import backtrader as bt
import os
from datetime import date, datetime
import importlib

parser = argparse.ArgumentParser()

# Take the value of capital to be used for the strategy.
parser.add_argument('--capital', default=100000.0,
                    help="Capital to start with")

# Take the name of the strategy from the user. The strategy should be in the
# strategies folder in a file named {strategy}.py.
parser.add_argument('--strategy', default=None, help="Strategy to use", choices=list(map(
    (lambda string: string.strip(".py")), os.listdir(os.path.join(config.root, "strategies")))))

# Take the symbols on which the backtest should be run. It should be specified
# in the config file.
parser.add_argument('--symbols', default=config.symbols,
                    nargs='+', choices=config.symbols, help="Symbols to use")

# Take the name of the file in which to store backtest results.
parser.add_argument('--name', default=datetime.now().strftime(
    "%I:%M%p-%B-%d-%Y"), help="Name of output file")

args = parser.parse_args()

# Import the strategy. The strategy file should contain a class called Backtest
# which inherits from bt.Strategy.
strategy_file = importlib.import_module(
    "strategies" + '.' + args.strategy)
strategy = getattr(strategy_file, "Backtest")


# Make sure the data is available.
os.system("python3 " + os.path.join(config.root, "data", "get.py"))

# Ensure that the results direcrory exists.
if not os.path.exists(os.path.join(config.root, "backtests", "results")):
    os.makedirs(os.path.join(config.root, "backtests", "results"))

for symbol in args.symbols:
    # Create a data feed.
    # Ten years worth of data starting from 1-1-2013 and ending on 31-12-2022
    # is used for backtesting.
    file = os.path.join(config.root, "data", (symbol + ".csv"))
    data = bt.feeds.GenericCSVData(dataname=file,
                                   fromdate=date(2013, 1, 1),
                                   todate=date(2023, 1, 1),
                                   dtformat=('%Y-%m-%d'),
                                   datetime=0,
                                   high=5,
                                   low=6,
                                   open=4,
                                   close=8,
                                   volume=10)

    # Run the backtest using Cerebro.
    cerebro = bt.Cerebro()  # Create a Cerebro entity.
    cerebro.broker.setcash(float(args.capital))  # Set the starting cash.
    cerebro.adddata(data)  # Add the data feed.
    cerebro.addstrategy(strategy)  # Add the trading strategies.

    # Specify file to store the results of the backtest.
    cerebro.addwriter(bt.WriterFile, csv=True, out=os.path.join(
        config.root, "backtests",  "results", args.name+".csv"))

    # Add analyzers.
    # TimeReturn is used to calculate the returns of the strategy.
    cerebro.addanalyzer(bt.analyzers.TimeReturn, _name='timereturn')
    # SharpeRatio is used to calculate the Sharpe Ratio of the strategy.
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharperatio')

    cerebro.run()  # Run the  simulation.
