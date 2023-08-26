import logging
import datetime

logging.basicConfig(
    filename=f'./movie_recommender/logs/{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)
logger = logging.getLogger()