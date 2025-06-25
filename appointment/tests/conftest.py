import pytest
from django.contrib.auth import get_user_model
from services.models import Service
from appointment.models import Appointment

@pytest.fixture
def create_user():
    User = get_user_model()
    return User.objects.create_user(email='client@example.com', password='password')

@pytest.fixture
def create_service():
    from services.models import Service
    return Service.objects.create(name="Haircut")

@pytest.fixture
def create_appointment(create_user, create_service):
    return Appointment.objects.create(
        user=create_user,
        service=create_service,
        date="2025-06-20",
        time="10:00"
    )