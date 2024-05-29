from services.mercado_bitcoin_api import MercadoBitcoinAPI
from utils.data_processing import get_historical_data
from utils.machine_learning import train_model
from utils.trading import execute_trading_strategy

def main():
    from config import API_KEY, API_SECRET

    api = MercadoBitcoinAPI(API_KEY, API_SECRET)

    # Obtém dados históricos
    btc_data = get_historical_data(api, 'BTC')
    
    # Treina o modelo
    model = train_model(btc_data)
    
    # Executa a estratégia de negociação
    execute_trading_strategy(api, model)

if __name__ == "__main__":
    main()
