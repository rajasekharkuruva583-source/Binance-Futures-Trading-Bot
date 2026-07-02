class TradingBotException(Exception):
    """Base exception for the trading bot."""
    pass


class ValidationException(TradingBotException):
    """Raised when user input is invalid."""
    pass


class BinanceAPIException(TradingBotException):
    """Raised when Binance returns an API error."""
    pass


class ConfigurationException(TradingBotException):
    """Raised when configuration is invalid."""
    pass