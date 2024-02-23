from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("counter/", views.counter, name="counter"),
    path("basic/", views.basic, name="basic")
]