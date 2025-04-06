import os

API_ID    = os.environ.get("API_ID", "24880064")
API_HASH  = os.environ.get("API_HASH", "70f62b60a6536d9653f35d1444c31335")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7919888960:AAEzGDJRn3k--czfvIE6W2Yv6azT37bce-4")

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
