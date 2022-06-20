import email
from django.test import TestCase, override_settings
from django.contrib.auth import authenticate
from django.http import HttpRequest
from django.contrib.auth import get_user_model
User = get_user_model()

class TestMasterPasswordBackend(TestCase):
    def createNewUser(self, username, email, password, is_staff=False, is_superuser=False):
        return User.objects.create_user(
            username = username,
            email = email,
            is_staff = is_staff,
            is_active = True,
            is_superuser = is_superuser,
            password = password,
        )

    def setUpNewUser(self):
        self.user_password = 'sample'
        self.user = self.createNewUser(
            username='sample',
            email='sample@sample.com',
            password=self.user_password,
        )

    def setUp(self):
        self.admin = self.createNewUser(
            username='admin',
            email='admin@admin.com',
            password='admin',
            is_staff=True,
            is_superuser=True,
        )
        self._login(self.admin)
    
    def _login(self, user):
        self.request = HttpRequest()
        self.request.user = user

    @override_settings(USE_ADMIN_USERNAME_FROM_SETTINGS=False)
    def test_valid_username_for_login_without_USE_ADMIN_USERNAME_FROM_SETTINGS(self):
        self.setUpNewUser()
        self.assertEqual(authenticate(request=self.request, username=self.user.username, password=self.user_password), self.user)
    
    @override_settings(USE_ADMIN_USERNAME_FROM_SETTINGS=False)
    def test_invalid_username_for_login_without_USE_ADMIN_USERNAME_FROM_SETTINGS(self):
        self.assertEqual(authenticate(request=self.request, username='sample', password='sample'), self.admin)

    @override_settings(
        USE_ADMIN_USERNAME_FROM_SETTINGS=True,
        ADMIN_LOGIN = 'admin',
    )
    def test_valid_admin_for_login_with_USE_ADMIN_USERNAME_FROM_SETTINGS(self):
        self.setUpNewUser()
        self.assertEqual(authenticate(request=self.request, username=self.user.username, password=self.user_password), self.user)

    @override_settings(
        USE_ADMIN_USERNAME_FROM_SETTINGS=True,
        ADMIN_LOGIN = 'not-you',
    )
    def test_invalid_admin_for_login_with_USE_ADMIN_USERNAME_FROM_SETTINGS(self):
        self.setUpNewUser()
        self.assertNotEqual(authenticate(request=self.request, username=self.user.username, password=self.user_password), self.user)
