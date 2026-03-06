import time

from scanner import scan
from exchange import fetch
from engine import open_position, check_close, open_trade
from assets import BTC
from config import TIMEFRAME, SCAN_INTERVAL


while True:

    # BTC análisis separado

    btc_df = fetch(BTC, TIMEFRAME)
    btc_price = btc_df.close.iloc[-1]

    check_close(btc_price)

    if open_trade is None:

        signals = scan()

        if signals:

            symbol, side, price = signals[0]

            open_position(symbol, side, price)

    time.sleep(SCAN_INTERVAL)
