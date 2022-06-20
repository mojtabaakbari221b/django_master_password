from django.contrib.auth.backends import BaseBackend
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

class MasterPasswordBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        if request is None :
            return
        user = request.user
        if user.is_authenticated and user.is_staff :
            use_admin_username_from_settings = getattr( settings, 'USE_ADMIN_USERNAME_FROM_SETTINGS', False )
            if use_admin_username_from_settings :
                if user.username == getattr( settings, 'ADMIN_LOGIN', None):
                    user = self.get_user_with_given_username(admin_user=user, username=username)
            else :
                user = self.get_user_with_given_username(admin_user=user, username=username)

            return user
    
    def get_user_with_given_username(self, admin_user, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = admin_user
        return user
