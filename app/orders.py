from app.client import place_order
from app.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)


class OrderService:

    @staticmethod
    def place_market_order(
        symbol,
        side,
        quantity,
    ):

        validate_symbol(symbol)
        validate_side(side)
        validate_order_type("MARKET")
        validate_quantity(quantity)

        return place_order(
            symbol=symbol,
            side=side,
            order_type="MARKET",
            quantity=quantity,
        )

    @staticmethod
    def place_limit_order(
        symbol,
        side,
        quantity,
        price,
    ):

        validate_symbol(symbol)
        validate_side(side)
        validate_order_type("LIMIT")
        validate_quantity(quantity)
        validate_price(price)

        return place_order(
            symbol=symbol,
            side=side,
            order_type="LIMIT",
            quantity=quantity,
            price=price,
        )