# -*- coding: utf-8 -*-
# @Author: Sep-aa
# @Date:   2026-02-04 09:25:57
# @Last Modified by:   Sep-aa
# @Last Modified time: 2026-02-04 10:48:04

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
