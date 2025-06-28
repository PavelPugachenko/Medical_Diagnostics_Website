from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import AppointmentForm


@login_required
def create_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect("/")
    else:
        form = AppointmentForm()
    return render(request, "appointment/form.html", {"form": form})
