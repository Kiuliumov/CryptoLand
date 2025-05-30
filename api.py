import dotenv
import os
import requests
dotenv.load_dotenv()

class API:
    def __init__(self):
        dotenv.load_dotenv()
        self.key = os.getenv('API_KEY')


class MarketEndpoint(API):
    pass

