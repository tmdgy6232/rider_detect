from django.urls import path, include
from detectapp.views import helloworld, detectme

app_name = 'detectapp'

urlpatterns = [
    path('hello/', helloworld, name='hello'),
    path('detect/', detectme, name='detect')
]