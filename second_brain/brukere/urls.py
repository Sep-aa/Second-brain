from django.urls import path
from . import views

urlpatterns = [
    path('brukere/', views.brukere, name='brukere'),
]