from flask import Flask
from celery import Celery

from flask import Flask

app = Flask(__name__)

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'

)

#
# setattr(Flask,'make_celery',make_celery)
# celery = app.make_celery()
celery = make_celery(app)





@celery.task()
def add_together(a, b):
    return a + b

@app.route('/add')
def task():
    result = add_together.delay(1,2)
    print(result.wait())
    return "ok"

if __name__ == "__main__":
    app.run()



