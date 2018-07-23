
from django.urls import path
from  . import views

urlpatterns = [

    path('', views.upload_excel, name="upload_excel"),
    path('uploadSuccess/', views.upload_success, name="upload_success"),
]
