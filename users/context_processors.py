from datetime import timedelta

from django.utils.timezone import now

from .models import Profile


def online_users(request):
    five_minutes_ago = now() - timedelta(minutes=5)
    count = Profile.objects.filter(last_seen__gte=five_minutes_ago).count()
    return {"online_users": count}
