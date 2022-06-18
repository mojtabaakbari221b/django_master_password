# django_master_password

this package is based on a simple idea, if you are a login as a site admin, Enter any password for each user, you can log in as that user .

## What is its use?
Absolutely clear, when users have a problem with their account and report to you, All you have to do is take their username from them without revealing their password information .

Installation
-----------------
Install via pip:
```
pip install django_master_password
```

Configuration
-----------------
*** AUTHENTICATION_BACKENDS ***
set this in settings.py :
```
AUTHENTICATION_BACKENDS = [
    'django_master_password.auth.backends.MasterPasswordBackend',
    'django.contrib.auth.backends.ModelBackend',
    ...
]
```
note : You can use any other backend instead of django.contrib.auth.backends.ModelBackend, but be sure to use it!
Because the package performs the login operation for you to observe the dry principle under certain conditions, and leaves the default login to the Django native classes.

*** USE_ADMIN_USERNAME_FROM_SETTINGS ***
If this value is true, only one user can log in to other users' accounts as an admin . (default is False)
Which user? The same username whose username is registered in ADMIN_LOGIN .

consider the following example :
```
USE_ADMIN_USERNAME_FROM_SETTINGS = True
ADMIN_LOGIN = 'superuser'
```

note : this is a good thing for you if you do not trust your admins :smile: :smile:

### Don't you think the package is very simple?
definitely yes, it's so simple that I do not even know why I packaged it,
but it's #funny, What better reason than this?
