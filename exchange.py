import requests
import pandas as pd

BASE = "https://api.binance.com/api/v3/klines"

def fetch(symbol, timeframe):

    params = {
        "symbol": symbol,
        "interval": timeframe,
        "limit": 200
    }

    r = requests.get(BASE, params=params)
    data = r.json()

    df = pd.DataFrame(data, columns=[
        "time","open","high","low","close","volume",
        "ct","qv","n","tb","tq","i"
    ])

    df[['open','high','low','close','volume']] = \
        df[['open','high','low','close','volume']].astype(float)

    return df
