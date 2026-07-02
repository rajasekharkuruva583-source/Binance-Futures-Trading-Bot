from app.constants import BUY, SELL, MARKET, LIMIT
from app.exceptions import ValidationException

def validate_symbol(symbol: str):
    if not symbol.endswith("USDT"):
        raise ValidationException("Only USDT trading pairs are supported.")


def validate_side(side: str):
    if side not in [BUY, SELL]:
        raise ValidationException("Side must be BUY or SELL.")


def validate_order_type(order_type: str):
    if order_type not in [MARKET, LIMIT]:
        raise ValidationException("Order type must be MARKET or LIMIT.")


def validate_quantity(quantity: float):
    if quantity <= 0:
        raise ValidationException("Quantity must be greater than zero.")


def validate_price(price: float):
    if price <= 0:
        raise ValidationException("Price must be greater than zero.")

