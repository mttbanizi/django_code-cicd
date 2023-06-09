from django.db import transaction 
from .models import BaseUser, Profile
from django.core.cache import cache


def create_profile(*, user:BaseUser, bio:str | None) -> Profile:
    return Profile.objects.create(user=user, bio=bio)

def create_user(*, email:str, password:str) -> BaseUser:
    return BaseUser.objects.create_user(email=email, password=password)


@transaction.atomic
def register(*, bio:str|None, email:str, password:str) -> BaseUser:

    user = create_user(email=email, password=password)
    create_profile(user=user, bio=bio)

    return user

def profile_count_update():
    profiles=cache.keys('profile_*')
    for profile_ley in profiles:
        email = profile_ley.replace("profile_", "")
        data = cache.get(profile_ley)

        try:
            profile = Profile.objects.get(user__email = email)
            profile.posts_count         = data.get("posts_count")
            profile.subscribers_count   = data.get("subscribers_count")
            profile.subscriptions_count = data.get("subscriptions_count")
        except Exception as ex:
            print(ex)



