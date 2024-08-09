from django.urls import path
from . import views

app_name = 'cement_strength'

urlpatterns = [
    path('', views.home, name='home'),

]
