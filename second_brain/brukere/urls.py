# -*- coding: utf-8 -*-
# @Author: Sep-aa
# @Date:   2026-01-28 13:41:04
# @Last Modified by:   Sep-aa
# @Last Modified time: 2026-02-04 11:27:41
from django.urls import path
from . import views

app_name = 'brukere'

urlpatterns = [
    path('brukere/', views.brukere, name='brukere'),
    path('brukere/detaljer/<int:id>', views.detaljer, name='detaljer'),
]