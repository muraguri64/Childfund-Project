from django.contrib import admin

# Register your models here.
from .models import Parentmasterlist

class parentMasterlistInfo(admin.ModelAdmin):
    list_display = (
                    'child_nbr', 'name', 'zone', 
                    'short_name', 'gender', 'date_of_birth', 
                    'sponsorship_start_date', 'contact_id', 'sponsor_name',
                    'parent_name', 'contact','id_number'
                   )
    list_filter = ('id', 'child_nbr', 'zone', 'date_of_birth','sponsorship_start_date','contact_id', 'sponsor_name')
    search_fields = ('name', 'child_nbr','parent_name', 'sponsor_name', 'zone')



admin.site.register(Parentmasterlist, parentMasterlistInfo)