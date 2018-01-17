import json
from django.shortcuts import HttpResponse


def hello(request):
    resp = {'nome' : 'ola'}
    return HttpResponse(json.dumps(resp), content_type="application/json")