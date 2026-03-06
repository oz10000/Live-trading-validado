def pidelta(df):

    ema = df.close.ewm(span=20).mean()

    deviation = (df.close - ema) / ema

    return deviation.iloc[-1]
