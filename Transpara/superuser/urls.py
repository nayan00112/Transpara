from django.urls import path
from . import views
urlpatterns = [
    path('', views.SuperUserInterface, name="SuperUserInterface"),
]