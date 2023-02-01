# This strategy merely serves as an example of how to add new strategies to the
# platform. It is not intended to be used as a trading strategy. It has been
# taken from backtrader's official documentation.Link to documentation :
# https://www.backtrader.com/docu/strategies/strategies.html#crossing-moving-averages
# A few modifications have been made to make it compatible with the platform.
# Each strategy file must contain a class called Backtest which is a subclass
# of backtrader.Strategy. This class is passed to a Cerebro instance created
# in backtest.py in order to do the backtesting. Each strategy file must also
# contain a function named scan which takes in recent data and checks if a
# trade can be taken based on the strategy.


import backtrader as bt
import pandas as pd
import ta


# Create a subclass of Strategy to define the indicators and logic
class Backtest(bt.Strategy):
    # list of parameters which are configurable for the strategy
    params = dict(
        pfast=10,  # period for the fast moving average
        pslow=30   # period for the slow moving average
    )

    def __init__(self):
        sma1 = bt.ind.SMA(period=self.p.pfast)  # fast moving average
        sma2 = bt.ind.SMA(period=self.p.pslow)  # slow moving average
        self.crossover = bt.ind.CrossOver(sma1, sma2)  # crossover signal

    def next(self):
        if not self.position:  # not in the market
            if self.crossover > 0:  # if fast crosses slow to the upside
                self.buy()  # enter long

        elif self.crossover < 0:  # in the market & cross to the downside
            self.close()  # close long position


# Create a function to scan recent data and check whether a trade can be taken
# based on this strategy or not.
def scan(data):
    # Calculate SMA using ta library.
    sma1 = ta.trend.sma_indicator(data['Close'], 10)
    sma2 = ta.trend.sma_indicator(data['Close'], 30)
    # Check if the fast moving average crosses the slow moving average to the
    # upside.
    if sma1.iloc[-1] > sma2.iloc[-1] and sma1.iloc[-2] < sma2.iloc[-2]:
        return 1
    # Check if the fast moving average crosses the slow moving average to the
    # downside.
    elif sma1.iloc[-1] < sma2.iloc[-1] and sma1.iloc[-2] > sma2.iloc[-2]:
        return -1
    else:
        return 0
