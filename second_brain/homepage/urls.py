# -*- coding: utf-8 -*-
# @Author: Sep-aa
# @Date:   2026-02-04 11:53:48
# @Last Modified by:   Sep-aa
# @Last Modified time: 2026-02-04 13:04:41
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
]