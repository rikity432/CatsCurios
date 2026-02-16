from django.utils.timezone import now

from .models import Profile


class UpdateLastSeenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            profile, _created = Profile.objects.get_or_create(user=request.user)

            # Avoid writing on every request; update at most once per minute.
            if profile.last_seen is None or (now() - profile.last_seen).total_seconds() > 60:
                profile.last_seen = now()
                profile.save(update_fields=["last_seen"])

        return self.get_response(request)
