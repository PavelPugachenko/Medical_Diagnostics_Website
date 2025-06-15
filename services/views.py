from django.shortcuts import get_object_or_404, redirect, render

from .forms import FeedbackForm
from .models import Feedback, Service


def service_list(request):
    services = Service.objects.all()
    return render(request, "services/list.html", {"services": services})


def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, "services/detail.html", {"service": service})


def home(request):
    return render(request, "services/home.html")


def index(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("index")  # Редирект на ту же страницу
    else:
        form = FeedbackForm()

    return render(request, "services/index.html", {"form": form})


def contact(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("feedback")  # Редирект на ту же страницу
    else:
        form = FeedbackForm()

    return render(request, "services/contact.html", {"form": form})
