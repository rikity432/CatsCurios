from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST

from .models import ChatMessage
from .utils import clean_message


@login_required
@require_POST
def send_message(request):
    msg = clean_message(request.POST.get("message", "")).strip()
    if not msg:
        return JsonResponse({"status": "empty"}, status=400)

    ChatMessage.objects.create(user=request.user, message=msg)
    return JsonResponse({"status": "ok"})


@login_required
@require_GET
def get_messages(request):
    qs = ChatMessage.objects.select_related("user").order_by("-created_at")[:20]
    messages = list(reversed(list(qs)))

    data = [
        {
            "user": m.user.username,
            "message": m.message,
            "created_at": m.created_at.isoformat(),
        }
        for m in messages
    ]

    return JsonResponse(data, safe=False)
