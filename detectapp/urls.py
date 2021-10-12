from django.urls import path, include
from detectapp.views import helloworld, detectme, ready, detail

app_name = 'detectapp'

urlpatterns = [
    path('hello/', helloworld, name='hello'),
    path('detect/', detectme, name='detect'),
    path('ready/', ready, name='ready'),
    path('detail/', detail, name='detail')
]