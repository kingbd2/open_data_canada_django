from django.db import models
import datetime
from django.utils import timezone
from postgres_copy import CopyManager

class Inventory(models.Model):
    ref_number = models.CharField(max_length=25, blank=True, null=True)
    title_en = models.CharField(max_length=75, blank=True, null=True)
    description_en = models.CharField(max_length=1000, blank=True, null=True)
    publisher_en = models.CharField(max_length=200, blank=True, null=True)
    date_published = models.DateField(null=True, blank=True)
    language = models.CharField(max_length=20, blank=True, null=True)
    size = models.BigIntegerField(null=True, blank=True, default=0)
    eligible_for_release = models.CharField(max_length=5, blank=True, null=True)
    program_alignment_architecture_en = models.CharField(max_length=75, blank=True, null=True)
    portal_url_en = models.CharField(max_length=200, blank=False, default='NaN')
    user_votes = models.IntegerField(default=0)
    owner_org = models.CharField(max_length=75, blank=True, null=True)
    owner_org_title = models.CharField(max_length=75, blank=True, null=True)
    objects = CopyManager()

    def __str__(self):
        return self.title_en
#
# MyModel.objects.from_csv(
#     "./data.csv",  # The path to a source file (a Python file object is also acceptable)
#     dict(name='NAME', number='NUMBER')  # A crosswalk of model fields to CSV headers.
# )
