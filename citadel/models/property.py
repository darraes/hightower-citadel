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

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1024)
    address = models.JSONField()
    size_m2 = models.IntegerField()
    bedrooms = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, default=None)
