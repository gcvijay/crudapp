import pytest
from django.urls import reverse
from app1.models import Registration
from django.core import mail
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.skipif('302 == 200')
@pytest.mark.django_db
@pytest.mark.parametrize('param',[
    ('registartion'),
    ('retrieve'),
])
def test_registration_view(client,param):
    url = reverse(param)
    response = client.get(url)
    assert response.status_code == 200
    #assertTemplateUsed(response, 'view_data.html','registration.html')
    assertTemplateUsed(response, 'registration.html')


    print("after the template ")
@pytest.mark.django_db
def test_create_view(client):
    url = reverse('create_daata')
    data = {
        'name': 'John',
        'sur_name': 'Doe',
        'mobile_number': '1234567890',
        'email': 'john@example.com',
        'age': 30,
        'occupation': 'Software Engineer'
    }
    resp = client.post(url, data=data)
    assert resp.status_code == 200


@pytest.fixture
def registration_data():
    return {
        'name': ['John','lakshmi','reddy'],
        'sur_name': 'Doe',
        'mobile': '1234567890',
        'email': 'john.doe@example.com',
        'age': '30',
        'occupation': 'Engineer'
    }
@pytest.mark.django_db
def test_data_insert(registration_data):
    assert Registration.objects.count() == 0
    Registration.objects.create(**registration_data)
    assert Registration.objects.count() == 1
#     model = Registration.objects.create(**registration_data)
#     assert model.objects.count() == 0

@pytest.mark.django_db
def test_edit_view(client, registration_data):
    # Create a registration object in the database
    registration = Registration.objects.create(**registration_data)

    # Get the edit page for the registration object
    url = reverse('edit', args=[registration.id])
    response = client.get(url)

    # Check that the response status code is 200 and the correct template is used
    assert response.status_code == 200
    assertTemplateUsed(response, 'edit.html')

    # Check that the response context contains the registration object
    assert 'object' in response.context
    assert response.context['object'] == registration


def test_email_sending(mailoutbox,settings):
    settings.EMAIL_BACKEND = 'django.core.mail.backemds.locmen.EmailBackend'
    assert len(mailoutbox) == 0
# from django.contrib.auth import get_user_model
# @pytest.mark.parametrize('param',[
#     ('registartion'),
#     ('create_daata'),
#     ('retrieve'),
#
# ])
# @pytest.mark.django_db
# def test_views(client,param):
#     temp_url = urls.reverse(param)
#     res = client.post(temp_url)
#
#     assert res.status_code == 200








