from exchange import fetch
from strategy import signal
from config import TIMEFRAME
from assets import ASSETS

def scan():

    signals = []

    for symbol in ASSETS:

        try:

            df = fetch(symbol, TIMEFRAME)

            s = signal(df)

            if s:
                price = df.close.iloc[-1]

                signals.append((symbol, s, price))

        except:
            pass

    return signals
