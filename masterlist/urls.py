
from django.urls import path
from  . import views

urlpatterns = [

    path('', views.upload_masterlist_excel, name="upload_masterlist_excel"),
    path('uploadSuccess/', views.upload_masterlist_success, name="upload_masterlist_success"),
]
