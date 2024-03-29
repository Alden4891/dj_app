from django.shortcuts import redirect
from django.urls import reverse

class AuthCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated and the request is not for the login view
        if not request.user.is_authenticated and not request.path.startswith(reverse('login')):
            return redirect('login')
        
        response = self.get_response(request)
        return response
