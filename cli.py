from app.constants import BUY, SELL, MARKET, LIMIT


def display_menu():

    print("\n" + "=" * 60)
    print("        BINANCE FUTURES TRADING BOT")
    print("=" * 60)

    print("1. Place Market Order")
    print("2. Place Limit Order")
    print("3. Exit")

#--------------

from app.constants import LIMIT
def get_float(prompt):

    while True:

        try:

            return float(input(prompt))

        except ValueError:

            print("❌ Please enter a valid number.")

def get_side():

    while True:

        side = input("Enter Side (BUY/SELL): ").strip().upper()

        if side in ["BUY", "SELL"]:
            return side

        print("❌ Invalid side. Please enter BUY or SELL.")

def get_symbol():

    while True:

        symbol = input("Enter Symbol (BTCUSDT): ").strip().upper()

        if symbol.endswith("USDT"):
            return symbol

        print("❌ Only USDT trading pairs are supported.")


def get_limit_order_input():

    print("\n----- Limit Order -----")

    symbol = get_symbol()

    side = get_side()

    quantity = get_float("Enter Quantity: ")

    price = get_float("Enter Price: ")

    return {
        "symbol": symbol,
        "side": side,
        "order_type": LIMIT,
        "quantity": quantity,
        "price": price,
    }

from app.constants import MARKET


def get_market_order_input():

    print("\n----- Market Order -----")

    symbol = get_symbol()

    side = get_side()

    quantity = get_float("Enter Quantity: ")

    return {
        "symbol": symbol,
        "side": side,
        "order_type": MARKET,
        "quantity": quantity,
    }


def confirm_order():

    while True:

        choice = input("\nConfirm Order? (Y/N): ").strip().upper()

        if choice in ["Y", "N"]:
            return choice == "Y"

        print("❌ Please enter Y or N.")


#------- Display Order Summary -----

def display_order_summary(data):

    print("\n" + "=" * 50)
    print("             ORDER SUMMARY")
    print("=" * 50)

    for key, value in data.items():
        print(f"{key.replace('_', ' ').title():18}: {value}")

    print("=" * 50)


#-------- Display Order Result----

def display_order_result(response):
    """
    Display Binance order response.
    """

    print("\n" + "=" * 50)
    print("        ORDER PLACED SUCCESSFULLY")
    print("=" * 50)

    print(f"Order ID        : {response.get('orderId')}")
    print(f"Client Order ID : {response.get('clientOrderId')}")
    print(f"Status          : {response.get('status')}")
    print(f"Symbol          : {response.get('symbol')}")
    print(f"Side            : {response.get('side')}")
    print(f"Order Type      : {response.get('type')}")
    print(f"Quantity        : {response.get('origQty')}")
    print(f"Executed Qty    : {response.get('executedQty')}")
    print(f"Price           : {response.get('price')}")
    print(f"Time In Force   : {response.get('timeInForce')}")

    print("=" * 50)

#---- Display Error -------

def display_error(error):
    """
    Display error message.
    """

    print("\n" + "=" * 50)
    print("            ORDER FAILED")
    print("=" * 50)

    print(f"Reason : {error}")

    print("=" * 50)