from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('brukere/', views.brukere, name='brukere'),
    path('brukere/detaljer/<int:id>', views.detaljer, name='detaljer'),
]