from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('landlord/', views.landlord_view, name='landlord_view'),
    path('tenant/', views.tenant_view, name='tenant_view'),
]