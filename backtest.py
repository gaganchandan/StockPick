import config
import argparse
import backtrader as bt
import os
import datetime
import importlib
from strategies.SMACrossover import Backtest

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
parser.add_argument('--name', default=datetime.datetime.now().strftime(
    "%I:%M%p-%B-%d-%Y"), help="Name of output file")

args = parser.parse_args()

# Import the strategy. The strategy file should contain a class called Backtest
# which inherits from bt.Strategy.
strategy_file = importlib.import_module(
    "strategies" + '.' + args.strategy)
strategy = getattr(strategy_file, "Backtest")


for symbol in args.symbols:
    # Check if the data has already been downloaded. If not, download it.
    try:
        assert (os.path.exists(os.path.join(
            config.root, "data", (symbol + ".csv"))))
    except AssertionError:
        exec(open(os.path.join(config.root, "data", "get.py")).read())

    # Create a data feed.
    csv = os.path.join(config.root, "data", (symbol + ".csv"))
    data = bt.feeds.GenericCSVData(dataname=csv,
                                   dtformat=('%Y-%m-%d'),
                                   datetime=0,
                                   high=5,
                                   low=6,
                                   open=4,
                                   close=8,
                                   volume=10)

    # Run the backtest using Cerebro.
    cerebro = bt.Cerebro()  # Create a Cerebro entity.
    cerebro.broker.setcash(args.capital)  # Set the starting cash.
    cerebro.adddata(data)  # Add the data feed.
    cerebro.addstrategy(strategy)  # Add the trading strategies.

    # Specify file to store the results of the backtest.
    cerebro.addwriter(bt.WriterFile, csv=True, out=os.path.join(
        config.root, "backtests", args.name+".csv"))

    cerebro.run()  # Run the  simulation.
