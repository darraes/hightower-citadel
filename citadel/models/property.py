from django.db import models

class Property(models.Model):
    class Meta(object):
        app_label = "citadel"
        indexes = [
            models.Index(
                fields=[
                    "deleted_at",
                ]
            )
        ]

    address = models.JSONField()
    size_m2 = models.IntegerField()
    bedrooms = models.IntegerField()
    created_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True)



