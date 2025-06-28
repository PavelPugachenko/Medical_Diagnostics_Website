import pytest
from services.models import Service, Feedback

@pytest.mark.django_db
def test_service_creation(sample_service):
    assert sample_service.title == "Test Service"
    assert sample_service.price == 99.99
    assert str(sample_service) == "Test Service"

@pytest.mark.django_db
def test_feedback_creation(feedback_data):
    feedback = Feedback.objects.create(**feedback_data)
    assert feedback.name == "Test User"
    assert feedback.email == "test@example.com"
    assert str(feedback) == f"Сообщение от Test User"