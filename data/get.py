import config
from nsepy import get_history
from datetime import date
import os

# Specify start and end date. 10 years worth of data will be used.
start = date(2013, 1, 1)
end = date(2022, 12, 31)

# Fetch historical data using nsepy.
for symbol in config.symbols:
    try:
        # Check if the data is already present. If not, download it.
        os.path.exists(os.path.join(config.root, "data", (symbol + ".csv")))
    except:
        data = get_history(symbol=symbol, start=start, end=end)
        # Save the data to a csv file.
        data.to_csv(os.path.join(config.root, "data", (symbol + ".csv")))
