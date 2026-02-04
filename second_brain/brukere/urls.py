# -*- coding: utf-8 -*-
# @Author: Sep-aa
# @Date:   2026-01-28 13:41:04
# @Last Modified by:   Sep-aa
# @Last Modified time: 2026-02-04 10:48:29
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('brukere/', views.brukere, name='brukere'),
    path('brukere/detaljer/<int:id>', views.detaljer, name='detaljer'),
]