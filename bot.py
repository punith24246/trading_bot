from binance.client import Client
from config import API_KEY, API_SECRET
from utils import log_info, log_error

class BasicBot:
    def __init__(self):
        # Initialize Binance Testnet client
        self.client = Client(API_KEY, API_SECRET, testnet=True)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            order_params = {
                'symbol': symbol,
                'side': side,
                'type': order_type,
                'quantity': quantity
            }

            if order_type == 'LIMIT' and price:
                order_params['price'] = price
                order_params['timeInForce'] = 'GTC'

            order = self.client.futures_create_order(**order_params)
            log_info(f"Order placed successfully: {order}")
            print(f"✅ Order successful: {order}")
            return order
        except Exception as e:
            log_error(f"Error placing order: {e}")
            print(f"❌ Failed to place order. Check logs for details.")
            return None
