from nsepy import get_history
from datetime import date

start = date(2013, 1, 1)
end = date(2022, 12, 31)

data = get_history(symbol="NIFTY", start=start, end=end, index=True)
data.to_csv("nifty.csv")
