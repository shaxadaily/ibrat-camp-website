from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('news_detail/<int:pk>/', news_detail, name='news_detail')
]