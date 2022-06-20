from django.test import TestCase, override_settings
from django.contrib.auth import authenticate
from django.http import HttpRequest
from django.contrib.auth import get_user_model
User = get_user_model()

class TestMasterPasswordBackend(TestCase):
    def setUp(self):
        self._password = 'admin'
        self.user = User.objects.create_user(
            username = 'admin',
            email = 'admin@admin.com',
            is_staff = True,
            is_active = True,
            is_superuser = True,
            password = 'admin',
        )

        self.request = HttpRequest()
        self.request.user = self.user

    @override_settings(USE_ADMIN_USERNAME_FROM_SETTINGS=False)
    def test_valid_username_for_login_without_USE_ADMIN_USERNAME_FROM_SETTINGS(self):
        pass
    
    @override_settings(USE_ADMIN_USERNAME_FROM_SETTINGS=False)
    def test_invalid_username_for_login_without_USE_ADMIN_USERNAME_FROM_SETTINGS(self):
        self.assertEqual(authenticate(request=self.request, username='sample', password='sample'), self.user)

    def test_valid_admin_for_login_with_USE_ADMIN_USERNAME_FROM_SETTINGS(self):
        pass

    def test_invalid_admin_for_login_with_USE_ADMIN_USERNAME_FROM_SETTINGS(self):
        pass