import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_index():
    client = Client()
    path = reverse('index')
    response = client.get(path)
    content = response.content.decode()
    expected_value = "<h1>Welcome to Holiday Homes</h1>"

    assert response.status_code == 200
    assert expected_value in content
