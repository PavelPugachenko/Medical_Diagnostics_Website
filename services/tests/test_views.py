import pytest
from django.urls import reverse
from django.test import Client
from services.models import Service, Feedback


# Тест главной страницы (home)
def test_home_view(client):
    url = reverse("home")
    response = client.get(url)

    assert response.status_code == 200
    assert "services/home.html" in [t.name for t in response.templates]


# Тест списка услуг (service_list)
def test_service_list_view(client, service):
    url = reverse("services:list")
    response = client.get(url)

    assert response.status_code == 200
    assert "services/list.html" in [t.name for t in response.templates]
    assert service in response.context["services"]


# Тест деталей услуги (service_detail)
def test_service_detail_view(client, service):
    url = reverse("services:detail", args=[service.pk])
    response = client.get(url)

    assert response.status_code == 200
    assert "services/detail.html" in [t.name for t in response.templates]
    assert response.context["service"] == service


# Тест формы обратной связи (index)
@pytest.mark.django_db
def test_index_view_get(client):
    url = reverse("index")
    response = client.get(url)

    assert response.status_code == 200
    assert "services/index.html" in [t.name for t in response.templates]
    assert "form" in response.context


@pytest.mark.django_db
def test_index_view_post_valid(client):
    url = reverse("index")
    data = {
        "name": "Иван",
        "email": "ivan@example.com",
        "message": "Хорошая клиника!",
    }
    response = client.post(url, data)

    # Проверяем редирект
    assert response.status_code == 302
    assert response.url == reverse("index")

    # Проверяем, что запись создалась
    assert Feedback.objects.count() == 1
    feedback = Feedback.objects.first()
    assert feedback.name == data["name"]
    assert feedback.email == data["email"]
    assert feedback.message == data["message"]


# Тест формы обратной связи (contact)
@pytest.mark.django_db
def test_contact_view_get(client):
    url = reverse("feedback")
    response = client.get(url)

    assert response.status_code == 200
    assert "services/contact.html" in [t.name for t in response.templates]
    assert "form" in response.context


@pytest.mark.django_db
def test_contact_view_post_valid(client):
    url = reverse("feedback")
    data = {
        "name": "Петр",
        "email": "petr@example.com",
        "message": "Нужна помощь!",
    }
    response = client.post(url, data)

    # Проверяем редирект
    assert response.status_code == 302
    assert response.url == reverse("feedback")  # Убедись, что такой URL существует

    # Проверяем, что запись создалась
    assert Feedback.objects.count() == 1
    feedback = Feedback.objects.first()
    assert feedback.name == data["name"]
    assert feedback.email == data["email"]
    assert feedback.message == data["message"]