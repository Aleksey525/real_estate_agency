# Generated by Django 2.2.24 on 2024-03-26 07:34

from django.db import migrations


def bind_owners_flats(apps, shema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    owners = Owner.objects.all()
    for owner in owners.iterator():
        flats = Flat.objects.filter(owner=owner.name)
        owner.flats.set(flats)
        owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20240326_1026'),
    ]

    operations = [migrations.RunPython(bind_owners_flats)
    ]
