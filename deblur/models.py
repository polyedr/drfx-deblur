from django.db import models
from jsonfield import JSONField


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """

    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class DeblurData(TimeStampedModel):
    deblur_data_text = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="uploads/", blank=True, null=True, max_length=256
    )
