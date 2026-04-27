import logging

logger = logging.getLogger("khel_ai")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter("[KHEL] %(asctime)s - %(message)s")

handler.setFormatter(formatter)
logger.addHandler(handler)
