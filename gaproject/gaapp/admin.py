from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Apartment, House, Item, Tenant, Payment

# Register your models here.
# class CustomUserAdmin(UserAdmin):
#     fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('role',)}))

# admin.site.register(User, CustomUserAdmin)
# admin.site.register(Apartment)
# admin.site.register(House)
# admin.site.register(Item)
# admin.site.register(Tenant)
# admin.site.register(Payment)
# gaapp/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Apartment, House, Item, Tenant, Payment

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Apartment)
admin.site.register(House)
admin.site.register(Item)
admin.site.register(Tenant)
admin.site.register(Payment)
