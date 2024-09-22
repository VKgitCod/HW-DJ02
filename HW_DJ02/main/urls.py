from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='second'),
    path('3', views.third, name='third'),
    path('4', views.fourth, name='fourth')
]
