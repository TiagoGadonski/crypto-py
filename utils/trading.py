import time

def execute_trading_strategy(api, model):
    while True:
        btc_ticker = api.get_ticker('BTC')
        current_price = float(btc_ticker['last'])

        prediction = model.predict([[current_price]])[0]
        print(f"Predicted price change: {prediction}")

        if prediction > 0.01:
            print("Buying BTC")
            api.place_order('BTC', 0.01, current_price, 'buy')
        elif prediction < -0.01:
            print("Selling BTC")
            api.place_order('BTC', 0.01, current_price, 'sell')

        time.sleep(60)
