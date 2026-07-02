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
    Returns authentication headers required by Binance.
    """
    return {
        "X-MBX-APIKEY": API_KEY
    }


def get_server_time():
    """
    Fetch Binance Futures server time.
    """

    logger.info("Fetching Binance Server Time...")

    url = f"{BASE_URL}/fapi/v1/time"

    response = requests.get(url)

    if response.status_code != 200:
        logger.error(response.text)
        raise BinanceAPIException(response.text)

    logger.info("Server Time Retrieved Successfully.")

    return response.json()


def get_account_info():
    """
    Fetch Binance Futures account information.
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

    logger.info("Fetching Account Information...")

    response = requests.get(
        url,
        headers=get_headers()
    )

    if response.status_code != 200:
        logger.error(response.text)
        raise BinanceAPIException(response.text)

    logger.info("Account Information Retrieved Successfully.")

    return response.json()


def place_order(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None,
):
    """
    Place MARKET or LIMIT order on Binance Futures.
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
        f"{key}={value}"
        for key, value in params.items()
    )

    signature = generate_signature(
        SECRET_KEY,
        query_string
    )

    url = (
        f"{BASE_URL}/fapi/v1/order?"
        f"{query_string}&signature={signature}"
    )

    # -------------------------------
    # Request Logging
    # -------------------------------
    logger.info("=" * 60)
    logger.info("REQUEST")
    logger.info("Endpoint : POST /fapi/v1/order")
    logger.info(f"Symbol   : {symbol}")
    logger.info(f"Side     : {side}")
    logger.info(f"Type     : {order_type}")
    logger.info(f"Quantity : {quantity}")

    if price is not None:
        logger.info(f"Price    : {price}")

    # -------------------------------
    # Send Request
    # -------------------------------
    response = requests.post(
        url,
        headers=get_headers()
    )

    # -------------------------------
    # Error Handling
    # -------------------------------
    if response.status_code != 200:

        logger.error("=" * 60)
        logger.error("BINANCE API ERROR")
        logger.error(response.text)
        logger.error("=" * 60)

        raise BinanceAPIException(response.text)

    # -------------------------------
    # Response Logging
    # -------------------------------
    logger.info("RESPONSE")
    logger.info(response.text)
    logger.info("=" * 60)

    return response.json()

