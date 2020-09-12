from django.urls import path
from . import views

# app_name = 'secondapp'
urlpatterns = [
    path('one/', views.one, name="page_one"),
]