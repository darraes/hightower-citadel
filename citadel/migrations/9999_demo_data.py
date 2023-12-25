from django.db import migrations
from citadel.models import Property


def add_data(apps, schema_editor):
    property_1 = Property.objects.create(
        address={
            "street": "122 Disney Springs",
            "city": "Orlando",
            "estate": "Florida",
            "zip": "51667",
            "country": "USA",
        },
        bedrooms = 4,
        size_m2 = 181,
    )


class Migration(migrations.Migration):
    dependencies = [
        ("citadel", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_data),
    ]
