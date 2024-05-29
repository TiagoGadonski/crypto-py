import requests
import pandas as pd

class MercadoBitcoinAPI:
    def __init__(self, api_key, api_secret):
        self.base_url = "https://www.mercadobitcoin.net/api"
        self.api_key = api_key
        self.api_secret = api_secret

    def get_ticker(self, coin):
        url = f"{self.base_url}/{coin}/ticker/"
        response = requests.get(url)
        data = response.json()
        return data['ticker']

    def get_trades(self, coin):
        url = f"{self.base_url}/{coin}/trades/"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data)
        df['price'] = df['price'].astype(float)
        df['date'] = pd.to_datetime(df['date'], unit='s')
        return df

    def place_order(self, coin, quantity, price, order_type='buy'):
        # Simulação de pedido - substitua pela implementação correta da API
        print(f"Placing {order_type} order for {quantity} {coin} at {price}")
        return {"status": "success"}
