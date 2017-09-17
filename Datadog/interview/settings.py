import logging

FORMAT = '%(levelname)s-%(name)s - %(funcName)s : %(message)s'
# FORMAT = '%(levelname)s-%(name)s-%(asctime)-20s - %(funcName)s : %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('Datadog')
logger.setLevel(logging.INFO)

CONSOLE_REFRESH_INTERVAL = 10
AVERAGE_TRAFFIC_TOLERANCE = 10
AVERAGE_TRAFFIC_INTERVAL = 120
