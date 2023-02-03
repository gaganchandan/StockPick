# StockPick

StockPick is a platform used for creating, backtesting and implementing custom trading stategies.

Installation:

1. Clone or download the repository from GitHub.

2. Go to the directory `StockPick` and run `pip install -r requirements.txt`.

3. Run `pip install -e .`.


Features:

1. Provides trade recommendations based on included strategies.

2. Enables viewing of price charts for selected stocks. 

3. Easily extensible. Simply create and add your strategies to the `strategies` folder and the rest will be taken care of automatically.

4. Uses latest data gathered using `nsepy`. Including new stocks is as easy as adding their names to `config.py`.

5. Effortless and customizable backtesting using `backtrader`.


Components:

1. `backtest.py`: A command line tool to run backtests quickly and easily. It is found under the `backtests` directory. For usage information, run `python3 backtest.py -h`. 

2. `stockpick.py`: Dashboard used for viewing recommended trades and price charts. It is found under the `stockpick` directory. 


Developed by:

[Gagan Chandan](https://github.com/gaganchandan)

[Daiwik Bhasker](https://github.com/daiwikR)

[Manish Naik](https://github.com/manishnaik69)


