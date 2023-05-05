from django.urls import path, include
from . import views

urlpatterns = [
    path('1/', views.test1, name = 'test-data-1'),
]