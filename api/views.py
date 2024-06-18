from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def StudentApi(request,id=None):
    if request.method=='GET':
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
    elif request.method=='POST':
        student_serialized=StudentSerializer(data=request.data)
        if student_serialized.is_valid():
            student_serialized.save()
            return Response({'Success':'Student Created'},status=status.HTTP_201_CREATED)
        return Response(student_serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='PUT':
        try:
            student=Student.objects.get(id=id)
            student_serialized=StudentSerializer(student,data=request.data)
            if student_serialized.is_valid():
                student_serialized.save()
                return Response({'Success':'Student Updated Fully'},status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({'Failed':'Student Not Found'},status=status.HTTP_400_BAD_REQUEST)
        return Response(student_serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='PATCH':
        try:
            student=Student.objects.get(id=id)
            student_serialized=StudentSerializer(student,data=request.data,partial=True)
            if student_serialized.is_valid():
                student_serialized.save()
                return Response({'Success':'Student Updated Partially'},status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({'Failed':'Student Not Found'},status=status.HTTP_400_BAD_REQUEST)
        return Response(student_serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        try:
            student=Student.objects.get(id=id)
            student.delete()
            return Response({'Success':'Student Deleted'},status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({'Failed':'Student Not Found'},status=status.HTTP_400_BAD_REQUEST)
    
    

