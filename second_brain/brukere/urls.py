# -*- coding: utf-8 -*-
# @Author: Sep-aa
# @Date:   2026-02-04 12:37:16
# @Last Modified by:   Sep-aa
# @Last Modified time: 2026-02-04 14:03:39
from django.urls import path
from . import views

urlpatterns = [
    path('', views.brukere, name='brukere'),
    path('detaljer/<int:id>', views.detaljer, name='detaljer'),
]