from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<slug:slug>', views.room_detail, name='room_detail'),
    path('set_afi_komen/<slug:slug>', views.set_afi_komen, name='set_afi_komen'),
]