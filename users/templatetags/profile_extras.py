from django import template
from django.templatetags.static import static

register = template.Library()


@register.filter
def profile_image_url(user, default_path: str = "users/default_profile.svg"):
    """Return a safe profile image URL for a user.

    - If the user has a Profile and an image, return its URL.
    - Otherwise, return a static default avatar.

    Works even when the OneToOne Profile row doesn't exist.
    """
    profile = getattr(user, "profile", None)
    if profile is None:
        return static(default_path)

    image_field = getattr(profile, "profile_image", None)
    if not image_field:
        return static(default_path)

    try:
        url = image_field.url
    except Exception:
        return static(default_path)

    return url or static(default_path)
