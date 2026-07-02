import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Binance API Configuration
API_KEY = os.getenv("BINANCE_API_KEY")
SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")
BASE_URL = os.getenv("BASE_URL")

#---- Exceptions ---

from app.exceptions import ConfigurationException

if not API_KEY:
    raise ConfigurationException(
        "API Key not found."
    )

if not SECRET_KEY:
    raise ConfigurationException(
        "Secret Key not found."
    )