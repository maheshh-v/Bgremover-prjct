from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('remove-bg/', views.remove_bg, name='remove_bg'),
] 