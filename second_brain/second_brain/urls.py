# -*- coding: utf-8 -*-
# @Author: Sep-aa
# @Date:   2026-02-04 11:53:48
# @Last Modified by:   Sep-aa
# @Last Modified time: 2026-02-04 14:03:48
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls')),
    path('brukere/', include('brukere.urls')),
    path('admin/', admin.site.urls),
]