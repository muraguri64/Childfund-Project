import xlrd
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Masterlist

# Create your views here.

def upload_masterlist_success(request):
    return render(request, 'masterlist/upload_masterlist_success.html')

def upload_masterlist_excel(request):
    if request.method == "POST":
        if request.FILES['excel']: 
               

            # Open the workbook and define the worksheet
            input_excel = request.FILES['excel']
            book = xlrd.open_workbook(file_contents=input_excel.read())
            sheet = book.sheet_by_index(0)

            insert_list = []
            for r in range(1, sheet.nrows):
                
                project_id             = sheet.cell(r,0).value
                case_nbr               = int(sheet.cell(r,1).value)
                child_nbr              = int(sheet.cell(r,2).value)
                child_name             = sheet.cell(r,3).value
                gender                 = sheet.cell(r,4).value
                date_of_birth          = str(sheet.cell(r,5).value)
                age                    = int(sheet.cell(r,6).value)
                child_status           = sheet.cell(r,7).value
              
                insert_list.append(Masterlist(project_id=project_id, case_nbr=case_nbr, 
                                                    child_nbr=child_nbr, child_name=child_name, 
                                                    gender=gender,date_of_birth=date_of_birth, 
                                                    age=age,child_status=child_status
                                                    ))


            Masterlist.objects.bulk_create(insert_list) 
            success_msg = "Successfully inserted {} records!".format(sheet.nrows-1)
            return redirect('upload_masterlist_success')


    else:    
        return render(request, 'masterlist/upload_masterlist.html')




    
