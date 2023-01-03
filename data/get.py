from config import *
from nsepy import get_history
from datetime import date
import os

# Specify start and end date
start = date(2013, 1, 1)
end = date(2022, 12, 31)

# Get Nifty data
data = get_history(symbol="NIFTY", start=start, end=end, index=True)
# Convert all values of Open, Close, High and Low to float
data = data.astype(float)
# Save the data to a csv file
data.to_csv(os.path.join(root, "data", "nifty.csv"))
