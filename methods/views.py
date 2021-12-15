from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from .models import NgrokUrl


# @csrf_exempt миксин чтобы не требовал токен
@csrf_exempt 
def setWebhook(request):
    text = request.GET.get('q', '')
    dataUrl = NgrokUrl.objects.all()[:1].get()
    print(dataUrl)
    if dataUrl:
        NgrokUrl.objects.all().update(NgrokUrl=text)
    else:
        b = NgrokUrl(NgrokUrl=text)
        b.save()
    
    return HttpResponse('request')


@csrf_exempt 
def rocketWebhook(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        data = json.dumps(data)
        print(data)
        header = {"Content-type": "application/json"}
        dataUrl = NgrokUrl.objects.all()[:1].get()
        print(dataUrl) 
        r = requests.post(dataUrl, data=data, headers=header)       
    return HttpResponse('request')
