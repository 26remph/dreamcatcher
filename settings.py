"""Settings environment module."""
import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
GOOGLE_TOKEN = os.getenv('GOOGLE_TOKEN')