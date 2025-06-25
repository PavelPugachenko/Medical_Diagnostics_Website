import pytest
from appointment.models import Appointment

def test_create_appointment(create_appointment):
    appointment = create_appointment
    assert appointment.user.email == 'client@example.com'
    assert appointment.service.name == "Haircut"
    assert str(appointment) == "client@example.com - Haircut"

def test_default_date(create_appointment):
    appointment = create_appointment
    assert appointment.date == "2025-06-20"

def test_default_time(create_appointment):
    appointment = create_appointment
    assert appointment.time.strftime("%H:%M") == "10:00"

def test_created_at_auto_now_add(create_appointment):
    appointment = create_appointment
    assert appointment.created_at is not None

def test_delete_user_deletes_appointment(create_user, create_service):
    appointment = Appointment.objects.create(
        user=create_user,
        service=create_service,
        date="2025-06-21",
        time="11:00"
    )
    create_user.delete()
    with pytest.raises(Appointment.DoesNotExist):
        appointment.refresh_from_db()

def test_delete_service_does_not_delete_appointment(create_user, create_service):
    appointment = Appointment.objects.create(
        user=create_user,
        service=create_service,
        date="2025-06-21",
        time="11:00"
    )
    create_service.delete()
    appointment.refresh_from_db()
    assert appointment.service is None