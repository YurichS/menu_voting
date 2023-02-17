import pytest
from rest_framework.test import APIClient
from accounts.models import Employee, Restaurant

client = APIClient()


@pytest.mark.django_db
def test_register_employee():
    url = '/account/register_employee/'
    data = dict(
        email="empl@mail.com",
        username="employee",
        password="1234",
        first_name="John",
        last_name="Teller"
    )
    client.post(url, data)
    assert Employee.objects.count() == 1


@pytest.mark.django_db
def test_register_restaurant():
    url = '/account/register_restaurant/'
    data = dict(
        email="rstnt@mail.com",
        username="restaurant",
        password="1234",
        name="Sweets and drinks",
        address="Ukraine"
    )
    client.post(url, data)
    assert Restaurant.objects.count() == 1


@pytest.mark.django_db
def test_login():
    # Create Employee
    url = '/account/register_employee/'
    data = dict(
        email="empl@mail.com",
        username="employee",
        password="1234",
        first_name="John",
        last_name="Teller"
    )
    client.post(url, data)

    # Create Restaurant
    url = '/account/register_restaurant/'
    data = dict(
        email="rstnt@mail.com",
        username="restaurant",
        password="1234",
        name="Sweets and drinks",
        address="Ukraine"
    )
    client.post(url, data)

    # Login tests
    url = '/account/login/'
    employee = dict(
        email="empl@mail.com",
        password="1234"
    )
    restaurant = dict(
        email="rstnt@mail.com",
        password="1234"
    )

    employee_response = client.post(url, employee)
    restaurant_response = client.post(url, restaurant)

    assert employee_response.status_code == 200
    assert restaurant_response.status_code == 200
