from flask import Flask
from core.scheduler_service import SchedulerService
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'formatter': 'default'
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)

@app.route('/', defaults = {'duration': 5})
@app.route('/<int:duration>', defaults = {'duration': 5})
def index(duration:int):
    return 'This is my first API call!'


@app.route('/pause')
def stop():
    scheduler_service.scheduler.pause()
    return 'Scheduler paused'

@app.route('/resume')
def resume():
    scheduler_service.scheduler.resume()
    return 'Scheduler started'

@app.route('/configuration/refresh')
def refresh():
    scheduler_service.add_configuration_tasks()
    return 'Scheduler updated'

scheduler_service = SchedulerService()