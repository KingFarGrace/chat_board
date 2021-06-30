import logging.handlers

handler = logging.FileHandler('app.log', encoding='utf-8')
handler.setLevel(logging.INFO)
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(lineno)s - %(message)s')
handler.setFormatter(logging_format)
logging.getLogger().addHandler(handler)
