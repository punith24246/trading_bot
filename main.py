from bot import BasicBot

def main():
    bot = BasicBot()

    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("Enter side (BUY or SELL): ").upper()
    order_type = input("Enter order type (MARKET or LIMIT): ").upper()
    quantity = float(input("Enter quantity (e.g., 0.001): "))

    price = None
    if order_type == 'LIMIT':
        price = input("Enter limit price (e.g., 30000): ")

    bot.place_order(symbol, side, order_type, quantity, price)

if __name__ == "__main__":
    main()
