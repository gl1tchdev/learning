from . import config
from celery import Celery

def get_app() -> Celery:
    app = Celery('rpc', 
             broker=config.BROKERS['rabbit'], backend=config.BROKERS['redis'])
    return app

celery = get_app()