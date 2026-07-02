# import hmac
# import hashlib


# def generate_signature(secret_key: str, query_string: str) -> str:
#     """
#     Generate HMAC SHA256 signature required by Binance.
#     """

#     return hmac.new(
#         secret_key.encode("utf-8"),
#         query_string.encode("utf-8"),
#         hashlib.sha256,
#     ).hexdigest()

# #-- After we'll delete above code....

import hashlib
import hmac


def generate_signature(secret_key: str, query_string: str) -> str:
    """
    Generate Binance HMAC SHA256 signature.
    """

    return hmac.new(
        secret_key.encode("utf-8"),
        query_string.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()
