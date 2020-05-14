
from django.urls import path
from user import views

urlpatterns = [
    path('index',views.index),
    path('dashboard',views.dashboard),
]
