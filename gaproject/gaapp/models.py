from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    ROLE_CHOICES = [
        ('landlord', 'Landlord'),
        ('tenant', 'Tenant'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    groups = models.ManyToManyField(Group, related_name='gaapp_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='gaapp_user_permissions_set', blank=True)

class Apartment(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    number_of_houses = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class House(models.Model):
    name = models.CharField(max_length=100)
    house_type = models.CharField(max_length=100, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='houses')
    image = models.ImageField(upload_to='house_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='items')
    
    def __str__(self) -> str:
        return f'{self.quantity} {self.name} in {self.house.name}'

class Tenant(models.Model):
    move_in_date = models.DateField()
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='tenants')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tenant_profile')

    def __str__(self):
        return self.user.username

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField()
    is_paid = models.BooleanField(default=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='payments')
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='payments')

    def __str__(self):
        return f'{self.amount} - {self.date_paid} - {"Paid" if self.is_paid else "Unpaid"}'

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

@receiver(post_save, sender=Tenant)
@receiver(post_delete, sender=Tenant)
def update_house_availability(sender, instance, **kwargs):
    house = instance.house
    if house:
        house.is_available = not house.tenants.exists()
        house.save()
