from django.urls import path
from . import views

urlpatterns = [
    path('',views.primera),
    path('solucion2/',views.solucion2)
    
    ]