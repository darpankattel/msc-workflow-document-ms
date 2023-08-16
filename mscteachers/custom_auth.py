from django.contrib.auth.backends import ModelBackend
from thesis.models import Coordinator


class CustomAdminBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = super().authenticate(request, username, password, **kwargs)
        if user:
            if Coordinator.objects.filter(user=user).exists():
                return user
        
        return None
