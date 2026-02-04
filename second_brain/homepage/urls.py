# -*- coding: utf-8 -*-
# @Author: Sep-aa
# @Date:   2026-02-04 09:28:26
# @Last Modified by:   Sep-aa
# @Last Modified time: 2026-02-04 10:48:12

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
