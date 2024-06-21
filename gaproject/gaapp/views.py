from django.shortcuts import render
from .models import Apartment, House, Item, Tenant, Payment
from .decorators import role_required

# Create your views here.
def home(request):
    apartments = Apartment.objects.all()
    return render(request, 'gaapp/home.html', {'apartments': apartments})


@role_required('landlord')
def landlord_view(request):
    # Landlord-specific view logic
    return render(request, 'gaapp/landlord.html')


@role_required('tenant')
def tenant_view(request):
    # Tenant-specific view logic
    return render(request, 'gaapp/tenant.html')
