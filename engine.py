import csv
from config import TP, SL
from metrics import Metrics

metrics = Metrics()

capital = 1000

open_trade = None

def open_position(symbol, side, price):

    global open_trade

    if side == "LONG":

        tp = price * (1 + TP)
        sl = price * (1 - SL)

    else:

        tp = price * (1 - TP)
        sl = price * (1 + SL)

    open_trade = {
        "symbol":symbol,
        "side":side,
        "entry":price,
        "tp":tp,
        "sl":sl
    }

    print("OPEN", open_trade)


def check_close(price):

    global open_trade
    global capital

    if open_trade is None:
        return

    side = open_trade["side"]
    entry = open_trade["entry"]
    tp = open_trade["tp"]
    sl = open_trade["sl"]

    closed = False

    if side == "LONG":

        if price >= tp:
            pnl = TP
            closed = True

        elif price <= sl:
            pnl = -SL
            closed = True

    else:

        if price <= tp:
            pnl = TP
            closed = True

        elif price >= sl:
            pnl = -SL
            closed = True

    if closed:

        metrics.update(pnl)

        capital *= (1 + pnl)

        log_trade(open_trade, price, pnl)

        print("CLOSE", pnl)
        print("WINRATE", metrics.winrate())
        print("CAPITAL", capital)

        open_trade = None


def log_trade(trade, price, pnl):

    with open("logs/trades.csv","a") as f:

        writer = csv.writer(f)

        writer.writerow([
            trade["symbol"],
            trade["side"],
            trade["entry"],
            price,
            pnl
        ])
