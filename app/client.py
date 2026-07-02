import time
import requests

from app.config import (
    API_KEY,
    SECRET_KEY,
    BASE_URL,
)

from app.logger import logger
from app.utils import generate_signature
from app.exceptions import BinanceAPIException


def get_headers():
    """
    Return Binance authentication headers.
    """

    return {
        "X-MBX-APIKEY": API_KEY
    }


def get_server_time():
    """
    Fetch Binance server time.
    """

    logger.info("Fetching Binance server time...")

    url = f"{BASE_URL}/fapi/v1/time"

    response = requests.get(url)

    if response.status_code != 200:

        logger.error(response.text)
        raise BinanceAPIException(response.text)

    return response.json()

# ---- Account info ---------

def get_account_info():
    """
    Fetch Futures account information.
    """

    timestamp = int(time.time() * 1000)

    query_string = f"timestamp={timestamp}"

    signature = generate_signature(
        SECRET_KEY,
        query_string
    )

    url = (
        f"{BASE_URL}/fapi/v2/account?"
        f"{query_string}&signature={signature}"
    )

    logger.info("Requesting account information")

    response = requests.get(
        url,
        headers=get_headers()
    )

    if response.status_code != 200:
    
            logger.error(response.text)
            raise BinanceAPIException(response.text)

    logger.info("Account information received")

    return response.json()

#---------
def place_order(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
):
    """
    Place an order on Binance Futures.
    """

    timestamp = int(time.time() * 1000)

    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
        "timestamp": timestamp,
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    query_string = "&".join(
        f"{key}={value}" for key, value in params.items()
    )

    signature = generate_signature(
        SECRET_KEY,
        query_string
    )

    url = (
        f"{BASE_URL}/fapi/v1/order?"
        f"{query_string}&signature={signature}"
    )

    logger.info(f"Placing {order_type} order")

    response = requests.post(
        url,
        headers=get_headers()
    )

    if response.status_code != 200:
    
            logger.error(response.text)
            raise BinanceAPIException(response.text)

    logger.info("Order placed successfully")

    return response.json()