from django.db import models


# Create your models here.
class Masterlist(models.Model):
    project_id = models.CharField(max_length=255, null=True, blank=True)
    case_nbr = models.IntegerField(null=True, blank=True)
    child_nbr = models.IntegerField(null=True, blank=True)
    child_name = models.CharField(max_length=255, null=True, blank=True)   
    gender = models.CharField(max_length=25, null=True, blank=True)
    date_of_birth = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    child_status = models.CharField(max_length=255, null=True, blank=True)
    

    def __str__(self):
        return self.child_name
