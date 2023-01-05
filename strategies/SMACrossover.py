# This strategy merely serves as an example of how to add new strategies to the
# platform. It is not intended to be used as a trading strategy. It has been
# taken from backtrader's official documentation.Link to documentation :
# https://www.backtrader.com/docu/strategies/strategies.html#crossing-moving-averages
# A few modifications have been made to make it compatible with the platform.
# Each strategy file must contain a class called Backtest which is a subclass
# of backtrader.Strategy.


import backtrader as bt


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
