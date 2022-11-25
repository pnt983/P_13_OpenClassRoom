import pytest
from django.test import Client
from django.urls import reverse
from .models import User, Profile


@pytest.mark.django_db
def test_profiles_index():
    client = Client()
    path = reverse('profiles_index')
    response = client.get(path)
    content = response.content.decode()
    expected_value = "<h1>Profiles</h1>"

    assert response.status_code == 200
    assert expected_value in content


@pytest.mark.django_db
def test_profiles_profile():
    client = Client()
    user = User.objects.create_user(
        username='test_username',
        first_name='test_first_name',
        last_name='test_last_name',
        email='email@test.com'
    )
    profile = Profile.objects.create(
        user=user,
        favorite_city="test_fav_city"
    )
    path = reverse('profile', args=[profile.user.username])
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<h1>test_username</h1>"

    assert response.status_code == 200
    assert expected_content in content
