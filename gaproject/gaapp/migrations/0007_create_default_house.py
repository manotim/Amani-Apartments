# gaapp/migrations/XXXX_create_default_house.py

from django.db import migrations, models

def create_default_house(apps, schema_editor):
    Apartment = apps.get_model('gaapp', 'Apartment')
    House = apps.get_model('gaapp', 'House')

    default_apartment, created = Apartment.objects.get_or_create(
        name='Default Apartment',
        defaults={'address': '123 Default St', 'number_of_houses': 1}
    )

    House.objects.get_or_create(
        name='Default House',
        defaults={'house_type': 'Default Type', 'is_available': True, 'apartment': default_apartment}
    )

class Migration(migrations.Migration):

    dependencies = [
        ('gaapp', '0006_alter_tenant_house'),  # Replace with the name of your latest migration file
    ]

    operations = [
        migrations.RunPython(create_default_house),
    ]
