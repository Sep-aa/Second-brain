# -*- coding: utf-8 -*-
# @Author: Sep-aa
# @Date:   2026-02-04 09:25:57
# @Last Modified by:   Sep-aa
# @Last Modified time: 2026-02-04 10:55:18

from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
    return render(request, 'index.html')

def brukere(request):
    return redirect('brukere:brukere')