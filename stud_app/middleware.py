from django.shortcuts import redirect
from django.urls import reverse

class MYMiddleware:
    """Custom auth enforcement middleware.

    If the user is not authenticated, redirect to login page for app pages.
    Skip login/logout/admin/static paths.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_paths = [
            '/login/',
            '/logout/',
            '/admin/',
            '/static/',
            '/media/',
        ]

        if not request.user.is_authenticated:
            for p in allowed_paths:
                if request.path.startswith(p):
                    return self.get_response(request)

            # Allow open root page if you want public entry point (optional)
            # if request.path == '/':
            #     return self.get_response(request)

            return redirect('login')

        return self.get_response(request)

