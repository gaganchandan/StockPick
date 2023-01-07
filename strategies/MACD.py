import backtrader as bt
import pandas as pd


class Backtest(bt.Strategy):
    params = (('period', 20),)

    def __init__(self):
        self.macd = bt.indicators.MACD(self.data)

    def next(self):
        if not self.position:
            if self.macd.macd > self.macd.signal:
                self.buy()
            elif self.macd.macd < self.macd.signal:
                self.close()
