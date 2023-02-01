import backtrader as bt
import ta


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


def scan(data):
    macd = ta.trend.macd(data['Close'], 20)
    if macd.iloc[-1] > 0 and macd.iloc[-2] < 0:
        return 1
    elif macd.iloc[-1] < 0 and macd.iloc[-2] > 0:
        return -1
    else:
        return 0
