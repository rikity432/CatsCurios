def csp_nonce(request):
    """Expose the per-request CSP nonce to templates."""

    return {"csp_nonce": getattr(request, "csp_nonce", "")}
