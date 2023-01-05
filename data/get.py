import config
from nsepy import get_history
from datetime import date, datetime
import os
import pandas as pd

# Specify start and end date. For the backtesting, ten years worth of data is
# used, starting from 1-1-2013 and ending on 31-12-2022. For live trading,
# the most recent data is used. Hence, the end date is set to the current date.
start = date(2013, 1, 1)
end = datetime.today().date()

# Fetch historical data using nsepy.
for symbol in config.symbols:
    file = os.path.join(config.root, "data", (symbol + ".csv"))
    try:
        # Check if the data is already present.
        assert (os.path.exists(file))
        # If the data is present, ensure that it is up to date.
        data = pd.read_csv(file)
        last_date = datetime.strptime(data.iloc[-1, 0], "%Y-%m-%d").date()
        if last_date < end:
            latest = get_history(symbol=symbol, start=last_date, end=end)
            data.concat(latest)
            print(data[-1])
            data.to_csv(file)
    except AssertionError:  # If the data is not present, download it.
        data = get_history(symbol=symbol, start=start, end=end)
        data.to_csv(file)
