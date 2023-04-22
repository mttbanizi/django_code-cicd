from celery import shared_task
from .services import profile_count_update

@shared_task
def hello1():
    print("HIIIII")

@shared_task
def profile_count_updates():
    profile_count_update()
