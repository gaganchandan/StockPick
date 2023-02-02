import backtrader as bt


def RSI(df):
    """
    Returns a pd.Series with the relative strength index.
    """
    close_delta = df['Close'].diff()
    period = 14
    # Make two series: one for lower closes and one for higher closes
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)
    # Use simple moving average
    ma_up = up.rolling(window=period).mean()
    ma_down = down.rolling(window=period).mean()
    rsi = ma_up / ma_down
    rsi = 100 - (100/(1 + rsi))
    return rsi


class Backtest(bt.Strategy):
    def __init__(self):
        self.rsi = bt.indicators.RSI_SMA(self.data)

    def next(self):
        if not self.position:
            if self.rsi < 30:
                self.buy()
        if self.position:
            if self.rsi > 70:
                self.close()


def scan(data):
    rsi = RSI(data)
    if rsi.iloc[-1] < 30:
        return 1
    elif rsi.iloc[-1] > 70:
        return -1
    else:
        return 0
