from pidelta import pidelta

THRESHOLD = 0.003

def signal(df):

    dev = pidelta(df)

    if dev < -THRESHOLD:
        return "LONG"

    if dev > THRESHOLD:
        return "SHORT"

    return None
