from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("service/", views.service_list, name="service_list"),
    path("<int:pk>/", views.service_detail, name="service_detail"),
    path("contact/", views.contact, name="feedback"),
]
