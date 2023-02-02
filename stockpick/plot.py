import config
import matplotlib.pyplot as plt
import os
import pandas as pd
import datetime


def plot_price_chart(symbol):
    end = datetime.date(2023, 2, 1)
    start = end - datetime.timedelta(days=90)
    file = os.path.join(config.root, "data", (symbol + '.csv'))
    data = pd.read_csv(file, index_col=False)
    data = data[['Date', 'Close']]
    data = data.set_index('Date')
    data.plot(figsize=(16, 9))
    plt.show()
