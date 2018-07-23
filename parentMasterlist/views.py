import xlrd
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Parentmasterlist

# Create your views here.

def upload_success(request):
    return render(request, 'parentMasterlist/upload_success.html')

def upload_excel(request):
    if request.method == "POST":
        if request.FILES['excel']: 
               

            # Open the workbook and define the worksheet
            input_excel = request.FILES['excel']
            book = xlrd.open_workbook(file_contents=input_excel.read())
            sheet = book.sheet_by_index(0)

            insert_list = []
            for r in range(1, sheet.nrows):
                
                child_nbr              = int(sheet.cell(r,0).value)
                name                   = sheet.cell(r,1).value
                zone                   = sheet.cell(r,2).value
                short_name             = sheet.cell(r,3).value
                gender                 = sheet.cell(r,4).value
                date_of_birth          = str(sheet.cell(r,5).value)
                sponsorship_start_date = str(sheet.cell(r,6).value)
                contact_id             = int(sheet.cell(r,7).value)
                sponsor_name           = sheet.cell(r,8).value
                parent_name            = sheet.cell(r,9).value
                contact                = int(sheet.cell(r,10).value)
                id_number              = int(sheet.cell(r,11).value)

                insert_list.append(Parentmasterlist(child_nbr=child_nbr, name=name, zone=zone,
                                                    short_name=short_name,gender=gender,date_of_birth=date_of_birth, 
                                                    sponsorship_start_date=sponsorship_start_date,contact_id=contact_id,
                                                    sponsor_name=sponsor_name, parent_name=parent_name,
                                                    contact=contact, id_number=id_number))


            Parentmasterlist.objects.bulk_create(insert_list) 
            success_msg = "Successfully inserted {} records!".format(sheet.nrows-1)
            return redirect('upload_success')


    else:    
        return render(request, 'parentMasterlist/upload.html')




    
