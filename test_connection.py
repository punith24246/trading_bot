from binance.client import Client
from config import API_KEY, API_SECRET

client = Client(API_KEY, API_SECRET, testnet=True)

try:
    info = client.futures_account()
    print("✅ Testnet API key is valid!")
    print(f"Total Wallet Balance: {info['totalWalletBalance']} USDT")
except Exception as e:
    print(f"❌ API connection failed: {e}")
