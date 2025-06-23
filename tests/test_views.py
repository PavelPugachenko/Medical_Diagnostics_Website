import pytest
from django.urls import reverse
from django.test import Client
from services.models import Service, Feedback


# Инициализируем клиент
@pytest.fixture
def client():
    return Client()


# Создаём тестовый сервис
@pytest.fixture
def service():
    return Service.objects.create(
        name="Стоматология",
        description="Лечение зубов",
        price=5000
    )


# Тест: страница service_list
def test_service_list_view(client, service):
    url = reverse("services:list")
    response = client.get(url)

    assert response.status_code == 200
    assert "services/list.html" in [t.name for t in response.templates]
    assert service in response.context["services"]


# Тест: страница service_detail
def test_service_detail_view(client, service):
    url = reverse("services:detail", args=[service.pk])
    response = client.get(url)

    assert response.status_code == 200
    assert "services/detail.html" in [t.name for t in response.templates]
    assert response.context["service"] == service


# Тест: страница home
def test_home_view(client):
    url = reverse("home")
    response = client.get(url)

    assert response.status_code == 200
    assert "services/home.html" in [t.name for t in response.templates]


# Тест: страница index — GET-запрос
def test_index_view_get(client):
    url = reverse("index")
    response = client.get(url)

    assert response.status_code == 200
    assert "services/index.html" in [t.name for t in response.templates]
    assert isinstance(response.context["form"], FeedbackForm)


# Тест: страница index — POST-запрос с валидной формой
def test_index_view_post_valid(client):
    url = reverse("index")
    data = {
        "name": "Иван",
        "email": "ivan@example.com",
        "message": "Хорошая клиника!",
    }
    response = client.post(url, data)

    # Проверяем, что редирект произошёл
    assert response.status_code == 302
    assert response.url == reverse("index")

    # Проверяем, что запись создалась
    assert Feedback.objects.count() == 1
    feedback = Feedback.objects.first()
    assert feedback.name == data["name"]
    assert feedback.email == data["email"]
    assert feedback.message == data["message"]


# Тест: страница contact — GET-запрос
def test_contact_view_get(client):
    url = reverse("contact")
    response = client.get(url)

    assert response.status_code == 200
    assert "services/contact.html" in [t.name for t in response.templates]
    assert isinstance(response.context["form"], FeedbackForm)


# Тест: страница contact — POST-запрос с валидной формой
def test_contact_view_post_valid(client):
    url = reverse("contact")
    data = {
        "name": "Петр",
        "email": "petr@example.com",
        "message": "Нужна помощь!",
    }
    response = client.post(url, data)

    # Проверяем редирект
    assert response.status_code == 302
    assert response.url == reverse("feedback")

    # Проверяем, что запись создалась
    assert Feedback.objects.count() == 1
    feedback = Feedback.objects.first()
    assert feedback.name == data["name"]
    assert feedback.email == data["email"]
    assert feedback.message == data["message"]