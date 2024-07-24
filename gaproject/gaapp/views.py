from django.shortcuts import render, get_object_or_404
from .models import Apartment, House, Item, Tenant, Payment
from .decorators import role_required

# Create your views here.
def home(request):
    apartments = Apartment.objects.all()
    return render(request, 'gaapp/home.html', {'apartments': apartments})

@role_required('landlord')
def landlord_view(request):
    houses = House.objects.all()
    items_for_houses = {f'items_for_house_{i+1}': house.items.all() for i, house in enumerate(houses)}
    context = {
        'houses': houses,
        'page_title': 'Landlord Dashboard',
        'landlord_username': request.user.username,
        **items_for_houses
    }
    return render(request, 'gaapp/landlord.html', context)


@role_required('tenant')
def tenant_view(request):
    # Tenant-specific view logic
    houses = House.objects.all()
    context = {
        'houses': houses,
        'page_title': 'Tenant Dashboard',
        'tenant_username': request.user.username,
    }
    return render(request, 'gaapp/tenant.html', context)


@role_required('tenant')
def house_items(request, house_id):
    house = get_object_or_404(House, id=house_id)
    items = house.items.all()
    return render(request, 'gaapp/house_items.html', {'house': house, 'items': items})