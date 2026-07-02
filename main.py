from cli import (
    display_menu,
    get_market_order_input,
    get_limit_order_input,
    confirm_order,
    display_order_summary,
    display_order_result,
    display_error,
)

from app.orders import OrderService


def main():

    while True:

        display_menu()

        choice = input("\nEnter Choice: ").strip()

        if choice == "1":

            data = get_market_order_input()

            display_order_summary(data)

            if confirm_order():

                try:

                    response = OrderService.place_market_order(
                        symbol=data["symbol"],
                        side=data["side"],
                        quantity=data["quantity"],
                    )

                    display_order_result(response)

                except Exception as error:

                    display_error(error)

            else:

                print("\nOrder Cancelled.")

            input("\nPress ENTER to continue...")


        elif choice == "2":

            data = get_limit_order_input()

            display_order_summary(data)

            if confirm_order():

                try:

                    response = OrderService.place_limit_order(
                        symbol=data["symbol"],
                        side=data["side"],
                        quantity=data["quantity"],
                        price=data["price"],
                    )

                    display_order_result(response)

                except Exception as error:

                    display_error(error)

            else:

                print("\nOrder Cancelled.")

            input("\nPress ENTER to continue...")


        elif choice == "3":

            print("\nThank you for using Binance Futures Trading Bot!")
            break

        else:

            print("\nInvalid Choice. Please select 1, 2 or 3.")

            input("\nPress ENTER to continue...")


if __name__ == "__main__":
    main()