from config import *
import argparse
import backtrader as bt
import os
import datetime

csv = os.path.join(root, "data", "nifty.csv")
data = bt.feeds.GenericCSVData(dataname=csv,
                               dtformat=('%Y-%m-%d'),
                               datetime=0,
                               high=2,
                               low=3,
                               open=1,
                               close=4,
                               volume=5)

parser = argparse.ArgumentParser()
parser.add_argument('--capital', default=100000.0,
                    help="Capital to start with")
parser.add_argument('--strategy', default=None, help="Strategy to use")
parser.add_argument('--name', default=datetime.datetime.now().strftime(
    "%I:%M%p-%B-%d-%Y"), help="Name of output file")
args = parser.parse_args()
strategy = importlib.import_module(os.path.join(
    root, strategies, (args.strategy+".Backtest")))

# Run the backtest using Cerebro
cerebro = bt.Cerebro()  # Create a Cerebro entity
cerebro.broker.setcash(args.capital)  # Set the starting cash
cerebro.adddata(data)  # Add the data feed
cerebro.addstrategy(strategy)  # Add the trading strategies
cerebro.run()  # Run the  simulation
