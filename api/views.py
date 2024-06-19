from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
class StudentApi(APIView):    

    def get(self,request,id=None,format=None):
        if id is not None:
            try:
                student=Student.objects.get(id=id)
                student_serialized=StudentSerializer(student)
                return Response(student_serialized.data,status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({'Failed':'Student Does not Exists'},status=status.HTTP_400_BAD_REQUEST)
        else:
            students=Student.objects.all()
            student_serialized=StudentSerializer(students,many=True)
            return Response(student_serialized.data,status=status.HTTP_200_OK)
        
    def post(self,request,format=None):
        student_serialized=StudentSerializer(data=request.data)
        if student_serialized.is_valid():
            student_serialized.save()
            return Response({'Success':'Student Created'},status=status.HTTP_201_CREATED)
        return Response(student_serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id=None,format=None):
        try:
            student=Student.objects.get(id=id)
            student_serialized=StudentSerializer(student,data=request.data)
            if student_serialized.is_valid():
                student_serialized.save()
                return Response({'Success':'Student Updated Fully'},status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({'Failed':'Student Not Found'},status=status.HTTP_400_BAD_REQUEST)
        return Response(student_serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,id=None,format=None):
        try:
            student=Student.objects.get(id=id)
            student_serialized=StudentSerializer(student,data=request.data,partial=True)
            if student_serialized.is_valid():
                student_serialized.save()
                return Response({'Success':'Student Updated Partially'},status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({'Failed':'Student Not Found'},status=status.HTTP_400_BAD_REQUEST)
        return Response(student_serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id=None,format=None):
        try:
            student=Student.objects.get(id=id)
            student.delete()
            return Response({'Success':'Student Deleted'},status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({'Failed':'Student Not Found'},status=status.HTTP_400_BAD_REQUEST)
        
    

