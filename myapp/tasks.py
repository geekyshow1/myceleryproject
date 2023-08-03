from celery import shared_task
from time import sleep
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

@shared_task
def sub(x, y):
    sleep(10)
    return x - y

@shared_task
def clear_session_cache(id):
    print(f"Session Cache Cleared: {id}")
    return id

@shared_task
def clear_redis_data(key):
    print(f"Redis Data Cleared: {key}")
    return key

@shared_task
def clear_rabbitmq_data(key):
    print(f"RabbitMQ Data Cleared: {key}")
    return key

# Create Schedule every 30 seconds
schedule, created = IntervalSchedule.objects.get_or_create(
    every=30,
    period=IntervalSchedule.SECONDS,
)
# Schedule the periodic task programmatically
PeriodicTask.objects.get_or_create(
    name='Clear RabbitMQ Periodic Task',
    task='myapp.tasks.clear_rabbitmq_data',
    interval=schedule,
    args=json.dumps(['hello']),  # Pass the arguments to the task as a JSON-encoded list
)