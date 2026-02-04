# -*- coding: utf-8 -*-
# @Author: Sep-aa
# @Date:   2026-02-04 12:37:16
# @Last Modified by:   Sep-aa
# @Last Modified time: 2026-02-04 13:46:45
from django.urls import path
from . import views

urlpatterns = [
    path('', views.brukere, name='brukere'),
    path('<int:id>', views.detaljer, name='detaljer'),
]