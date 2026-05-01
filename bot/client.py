import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

BASE_URL = "https://testnet.binancefuture.com"

def get_client():
    client = Client(API_KEY, API_SECRET, testnet=True)
    client.FUTURES_URL = BASE_URL
    return client