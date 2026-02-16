from .models import Post


def cat_status(request):
    latest = Post.objects.filter(status=1).order_by("-created_on").first()
    return {
        "cat_status": latest.mood if latest else "Unknown",
    }
