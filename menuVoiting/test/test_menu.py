import pytest
from rest_framework.test import APIClient
from menu.models import Menu

client = APIClient()


def create_restaurant():
    """Function for creating a restaurant(allowed upload menu)"""
    url = '/account/register_restaurant/'
    data = dict(
        email="rstnt@mail.com",
        username="restaurant",
        password="1234",
        name="Sweets and drinks",
        address="Ukraine"
    )
    client.post(url, data)
    url = '/account/login/'
    restaurant = dict(
        email="rstnt@mail.com",
        password="1234"
    )
    client.post(url, restaurant)


@pytest.mark.django_db
def test_menu_upload():
    create_restaurant()
    url = '/menu/menu_upload/'
    data = dict(menu="menu_for_today", restaurant=3)
    client.post(url, data)
    assert Menu.objects.count() == 1


@pytest.mark.django_db
def test_menu_list():
    # create menu
    create_restaurant()
    url = '/menu/menu_upload/'
    data = dict(menu="menu_for_today", restaurant=3)
    client.post(url, data)
    # test menu_list
    response = client.get("/menu/menu_list/")
    assert response.status_code == 200

