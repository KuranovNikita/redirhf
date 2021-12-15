from django.urls import path
from methods.views import *

urlpatterns = [
    path('setWebhook', setWebhook),
    path('rocketWebhook', rocketWebhook),
]