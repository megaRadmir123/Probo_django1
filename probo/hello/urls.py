from django.urls import path
from . import views

urlpetterns = [
    path('',views.index,name='index'),
    path('zameki/<int:zametka_id>/',views.zametka,name='zametka'),
]
