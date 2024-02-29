# conftest.py

def pytest_configure():
    from django.conf import settings

    settings.configure(
        DEBUG=False,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:'
            }
        },
        INSTALLED_APPS=[
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'app1',
        ],
        ROOT_URLCONF='crudapp.urls',
        SECRET_KEY='your_secret_key',
        MIDDLEWARE=[],
        TIME_ZONE='UTC',
    )

# import pytest
# @pytest.fixture
# def registration_data():
#     return {
#         'name': 'John',
#         'sur_name': 'Doe',
#         'mobile': '1234567890',
#         'email': 'john.doe@example.com',
#         'age': 30,
#         'occupation': 'Engineer'
#     }




