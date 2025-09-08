def get_user_input():
    symbol = input('Enter symbol (e.g., BTCUSDT): ').strip().upper()
    side = input('Enter side (BUY or SELL): ').strip().upper()
    order_type = input('Enter order type (MARKET or LIMIT): ').strip().upper()
    quantity = float(input('Enter quantity (e.g., 0.001): '))
    price = None

    if order_type == 'LIMIT':
        price = float(input('Enter price (e.g., 50000): '))

    return symbol, side, order_type, quantity, price
