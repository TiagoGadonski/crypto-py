import time
import pandas as pd

def get_historical_data(api, coin, limit=1000):
    trades = []
    while len(trades) < limit:
        new_trades = api.get_trades(coin)
        trades.extend(new_trades)
        trades = list({v['tid']: v for v in trades}.values())  # Remove duplicatas
        if len(trades) >= limit:
            break
        time.sleep(1)  # Evitar sobrecarregar a API
    df = pd.DataFrame(trades)
    df['price'] = df['price'].astype(float)
    df['date'] = pd.to_datetime(df['date'], unit='s')
    return df
