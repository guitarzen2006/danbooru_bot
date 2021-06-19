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

def log_start_app(name):
    ''' This fuction is for when the bot.py app starts '''
    return logger.info(f"The {name} application has started.")

def log_app_request(limit_amount, user):
    return logger.info(f"{user} has requested {limit_amount} pics.")

def log_app_failure(message):
    return logger.warn(message)

def log_api_http_response_200(http_response_code_200):
    return logger.info(http_response_code_200)

def log_api_http_response_error(http_response_code_error):
    return logger.error(http_response_code_error)

