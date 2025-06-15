import pytest
from django.urls import reverse
from .models import Appointment

@pytest.mark.django_db
def test_model_creation():
    """Проверка создания модели"""
    obj = Appointment.objects.create(name="Test Object")
    assert obj.name == "Test Object"
