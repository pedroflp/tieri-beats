from django.urls import path
from . import views

urlpatterns = [
    path('', views.beats, name='beats'),
    path('beats/', views.beats, name='beats'),
    path('freecopyright/', views.freecopyright, name='freecopyright'),
    path('pricing/', views.pricing, name='pricing'),
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact, name='contact'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('pricing/checkout/', views.checkout, name='checkout'),
]