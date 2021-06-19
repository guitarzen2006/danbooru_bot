import logging

# see https://realpython.com/python-logging/

# instaniate handler
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger_format = logging.Formatter('%(asctime)s-%(levelno)s-%(levelname)s-%(name)s- %(message)s')

# Create logging handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('app.log')

# Set logging attributes
console_handler.setFormatter(logger_format)
file_handler.setFormatter(logger_format)

# Add handlers to the 'logger'
logger.addHandler(console_handler)
logger.addHandler(file_handler)

def start_log(name):
    return logger.info(f"The {name} application has started.")

def log_request(limit_amount, user):
    return logger.info(f"{user} has requested {limit_amount} pics.")


