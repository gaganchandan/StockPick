# This program scans recent data to check for possible trades
# based on the strategies defined in the strategies folder. It
# considers all the strategies in the strategies folder and and
# all the stocks in config.py.


import config
import importlib
import os
import pandas as pd

# Make a list of all the strategies in the strategies folder.
strategies = list(map((lambda string: string.strip(".py")),
                      list(filter((lambda name: name.endswith(".py")),
                                  os.listdir(os.path.join(config.root, 'strategies'))))))

# Make a list of all the csv files in the data folder.
files = list(filter((lambda name: name.endswith(".csv")),
             os.listdir(os.path.join(config.root, 'data'))))

# Run the scans and store the calls in a list.
calls = []
for strategy in strategies:
    # Import the strategy.
    strategy_file = importlib.import_module('strategies' + '.' + strategy)
    try:
        scan = getattr(strategy_file, "scan")
    except AttributeError:
        continue

    for file in files:
        data = pd.read_csv(os.path.join(config.root, 'data', file))
        if scan(data) == 1:
            calls.append("Buy " + file.strip(".csv") + " based on " + strategy)
        if scan(data) == -1:
            calls.append("Close positions of " +
                         file.strip(".csv") + " based on " + strategy)

# Print the calls.
print(calls)
