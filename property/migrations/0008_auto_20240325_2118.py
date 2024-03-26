from django.db import migrations
import phonenumbers


def formated_phone_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        pars_number = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if not phonenumbers.is_valid_number(pars_number):
            continue
        flat.owner_pure_phone = phonenumbers.format_number(pars_number, phonenumbers.PhoneNumberFormat.E164)
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [migrations.RunPython(formated_phone_number)
    ]
