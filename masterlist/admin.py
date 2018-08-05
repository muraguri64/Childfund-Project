from django.contrib import admin

# Register your models here.
from .models import Masterlist

class masterlistInfo(admin.ModelAdmin):
    list_display = (
                    'project_id', 'case_nbr', 'child_nbr', 'child_name', 
                    'gender', 'date_of_birth', 'age', 'child_status' 
                    
                   )
    list_filter = ('project_id', 'case_nbr', 'child_nbr', 'gender', 'date_of_birth', 'child_name')
    search_fields = ('child_name', 'child_nbr','case_nbr', 'project_id')



admin.site.register(Masterlist, masterlistInfo)