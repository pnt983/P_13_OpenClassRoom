import pytest
from django.test import Client
from .models import Address, Letting
from django.urls import reverse


@pytest.mark.django_db
def test_lettings_index():
    client = Client()
    path = reverse('lettings_index')
    response = client.get(path)
    content = response.content.decode()
    expected_value = "<title>Lettings</title>"

    assert response.status_code == 200
    assert expected_value in content


@pytest.mark.django_db
def test_lettings_letting():
    client = Client()
    address = Address.objects.create(
        number=1,
        street='street_test',
        city='city_test',
        state='state_test',
        zip_code=11111,
        country_iso_code='FR')
    letting = Letting.objects.create(
        title='title_test',
        address=address
    )

    path = reverse('letting', args=(letting.id,))
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>title_test</title>"

    assert response.status_code == 200
    assert expected_content in content
