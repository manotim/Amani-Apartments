from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('landlord/', views.landlord_view, name='landlord_view'),
    path('tenant/', views.tenant_view, name='tenant_view'),
    path('houses/', views.house_list, name='house_list'),
    path('house/<int:house_id>/items/', views.house_items, name='house_items'),
    path('onebr_make_payment/', views.onebedroom_payment, name='onebedroom_payment'),
    path('bedsitter_make_payment/', views.bedsitter_payment, name='bedsitter_payment'),
]