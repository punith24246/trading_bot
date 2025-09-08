import logging
import os

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

# Logging configuration
logging.basicConfig(
    filename='logs/bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)
