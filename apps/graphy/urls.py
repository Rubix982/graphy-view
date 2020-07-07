from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('dashboard', views.dashboard, name="dashboard")
]

