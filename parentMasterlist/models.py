from django.db import models

# Create your models here.

# Create your models here.
class Parentmasterlist(models.Model):
    child_nbr = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    zone = models.CharField(max_length=255, null=True, blank=True)
    short_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=25, null=True, blank=True)
    date_of_birth = models.CharField(max_length=255, null=True, blank=True)
    sponsorship_start_date = models.CharField(max_length=255, null=True, blank=True)
    contact_id = models.IntegerField(null=True, blank=True)
    sponsor_name = models.CharField(max_length=255, null=True, blank=True)
    parent_name = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)
    id_number = models.IntegerField(null=True, blank=True)

    

    def __str__(self):
        return self.name