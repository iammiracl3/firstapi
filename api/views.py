from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from api import serializers
# Create your views here.
class StudentListEndPoint(APIView):
    def get(self, request):
        students= Student.objects.all()
        serializer=StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"messages": "post added successfully", "data": serializer.data }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            Student.objects.get(pk.id)
        except Student.DoesNotExist:
            raise Response({"messages": "Data successfully updated"})
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    


def delete(self, request, id):
    try:
        Student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        raise Response({"error": "student does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    Student.delete()
    return Response({"message": "student deleted successfully"},status=status.HTTP_204_NO_CONTENT)