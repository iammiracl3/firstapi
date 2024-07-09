from django.urls import path
from .views import StudentListEndPoint

urlpatterns =[
    path('Student', StudentListEndPoint.as_view(), name= "students")
]