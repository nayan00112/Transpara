from django.urls import path
from . import views
urlpatterns = [
    path('history', views.history, name="history"),
    path('delete_histry', views.delete_histry, name="delete_histry"),
]