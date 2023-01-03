import argparse
import backtrader as bt
from pathlib import Path

global data
data_folder = Path("../data")
data_csv = data_folder / "nifty.csv"
data = bt.feeds.GenericCSVData(dataname=data_csv,
                               dtformat=('%Y-%m-%d'),
                               datetime=0,
                               high=2,
                               low=3,
                               open=1,
                               close=4,
                               volume=5),
parser = argparse.ArgumentParser()
parser.add_argument('--capital.', default=100000.0,
                    help="Capital to start with")
parser.add_argument('--strategy', default=None, help="Strategy to use")

cerebro = bt.Cerebro()  # Create a cerebro entity
cerebro.broker.setcash(100000.0)  # Set the starting cash
cerebro.adddata(data)  # Add the data feed
cerebro.addstrategy()  # Add the trading strategies
cerebro.run()
