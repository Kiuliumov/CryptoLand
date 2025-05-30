import dotenv
import os
import requests
dotenv.load_dotenv()


class API:
    def __init__(self):
        self.key = os.getenv('API_KEY')
        self.base_url = 'https://rest.coinapi.io/v1/'

    def make_request(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        headers = {
            'X-CoinAPI-Key': self.key
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()


class MarketEndpoint(API):
    def get_exchange_rates(self, asset_id_base, asset_id_quote):
        endpoint = f"exchangerate/{asset_id_base}/{asset_id_quote}"
        return self.make_request(endpoint)

    def list_assets(self):
        endpoint = "assets"
        return self.make_request(endpoint)

