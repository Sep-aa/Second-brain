# -*- coding: utf-8 -*-
# @Author: Sep-aa
# @Date:   2026-02-04 12:13:12
# @Last Modified by:   Sep-aa
# @Last Modified time: 2026-02-04 13:40:52
from django.http import HttpResponse
from django.template import loader

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())