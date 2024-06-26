from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="homepage"),
    path("add/", views.add, name="addpage"),
    path("view-edit/<int:event_pk>", views.view_edit)
]