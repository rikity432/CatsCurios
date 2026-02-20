import secrets

from django.conf import settings


class ContentSecurityPolicyMiddleware:
    """Add a CSP header (and per-request nonce) in production.

    This is aimed at improving Lighthouse "Best Practices" by:
    - eliminating mixed-content where possible (upgrade-insecure-requests)
    - providing an enforcement-mode CSP header

    Note: We intentionally do not enable Trusted Types here because the app
    currently uses DOM APIs like innerHTML in a few places.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.csp_nonce = secrets.token_urlsafe(16)
        response = self.get_response(request)

        # Keep development friction low.
        if settings.DEBUG:
            return response

        nonce = getattr(request, "csp_nonce", "")

        # Allow required third-party CDNs currently used by templates.
        # Keep it reasonably strict while not breaking Bootstrap/FontAwesome/
        # Chart.js.
        csp = (
            "default-src 'self'; "
            "base-uri 'self'; "
            "object-src 'none'; "
            "frame-ancestors 'self'; "
            "img-src 'self' data: https://res.cloudinary.com; "
            "font-src 'self' data: https://fonts.gstatic.com "
            "https://cdnjs.cloudflare.com; "
            "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net "
            "https://fonts.googleapis.com https://cdnjs.cloudflare.com; "
            f"script-src 'self' 'nonce-{nonce}' https://cdn.jsdelivr.net "
            "https://cdnjs.cloudflare.com; "
            "connect-src 'self'; "
            "upgrade-insecure-requests"
        )

        response.headers["Content-Security-Policy"] = csp
        return response
