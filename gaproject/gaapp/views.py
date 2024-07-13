from django.shortcuts import render
from .models import Apartment, House, Item, Tenant, Payment
from .decorators import role_required

# Create your views here.
def home(request):
    apartments = Apartment.objects.all()
    return render(request, 'gaapp/home.html', {'apartments': apartments})


# @role_required('landlord')
# def landlord_view(request):
#     houses = House.objects.all()
#     return render(request, 'gaapp/landlord.html', {'houses': houses})
@role_required('landlord')
def landlord_view(request):
    houses = House.objects.all()
    items_for_house_1 = []
    items_for_house_2 = []
    items_for_house_3 = []
    items_for_house_4 = []
    items_for_house_5 = []
    if len(houses) > 0:
        house_1 = houses[0]
        items_for_house_1 = house_1.items.all()
        
    if len(houses) > 1:
        house_2 = houses[1]
        items_for_house_2 = house_2.items.all()

    if len(houses) > 2:
        house_3 = houses[2]
        items_for_house_3 = house_3.items.all()

    if len(houses) > 3:
        house_4 = houses[3]
        items_for_house_4 = house_4.items.all()

    if len(houses) > 4:
        house_5 = houses[4]
        items_for_house_5 = house_5.items.all()

    if len(houses) > 5:
        house_6 = houses[5]
        items_for_house_6 = house_6.items.all()

    if len(houses) > 6:
        house_7 = houses[6]
        items_for_house_7 = house_7.items.all()

    if len(houses) > 7:
        house_8 = houses[7]
        items_for_house_8 = house_8.items.all()

    if len(houses) > 8:
        house_9 = houses[8]
        items_for_house_9 = house_9.items.all()

    if len(houses) > 9:
        house_10 = houses[9]
        items_for_house_10 = house_10.items.all()

    if len(houses) > 10:
        house_11 = houses[10]
        items_for_house_11 = house_11.items.all()

    if len(houses) > 11:
        house_12 = houses[11]
        items_for_house_12 = house_12.items.all()
        
    if len(houses) > 12:
        house_13 = houses[12]
        items_for_house_13 = house_13.items.all()

    if len(houses) > 13:
        house_14 = houses[13]
        items_for_house_14 = house_14.items.all()
              
    return render(request, 'gaapp/landlord.html', {'houses': houses, 'items_for_house_1': items_for_house_1, 'items_for_house_2': items_for_house_2, 'items_for_house_3': items_for_house_3, 'items_for_house_4': items_for_house_4, 'items_for_house_5': items_for_house_5, 'items_for_house_6': items_for_house_6, 'items_for_house_7': items_for_house_7, 'items_for_house_8': items_for_house_8, 'items_for_house_9': items_for_house_9, 'items_for_house_10': items_for_house_10, 'items_for_house_11': items_for_house_11, 'items_for_house_12': items_for_house_12, 'items_for_house_13': items_for_house_13, 'items_for_house_14': items_for_house_14})



@role_required('tenant')
def tenant_view(request):
    # Tenant-specific view logic
    return render(request, 'gaapp/tenant.html')
