from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('landlord/', views.landlord_view, name='landlord_view'),
    path('tenant/', views.tenant_view, name='tenant_view'),
     path('house/<int:house_id>/items/', views.house_items, name='house_items'),
]