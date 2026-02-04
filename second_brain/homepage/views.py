# -*- coding: utf-8 -*-
# @Author: Sep-aa
# @Date:   2026-02-04 12:13:12
# @Last Modified by:   Sep-aa
# @Last Modified time: 2026-02-04 12:53:02
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
    
def home(request):
    return redirect('brukere')