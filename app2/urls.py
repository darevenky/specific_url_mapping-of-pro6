from app2.views import *

from django.urls import path

app_name='nothing'

urlpatterns=[
    path('makram/',makram,name='makram'),
]