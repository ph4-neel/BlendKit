from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

# Create your views here.

class College(APIView):
    def Get(self,request):
        objs = Student.objects.all()
        serializer = CollegeSerializer(objs, many=True)
        return Response(serializer.data)

    def Post(self,request):
        data = request.data
        serializer = CollegeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)

class Department(APIView):
    def Get(self,request):
        objs = Student.objects.all()
        serializer = DepartmentSerializer(objs, many=True)
        return Response(serializer.data)

    def Post(self,request):
        data = request.data
        serializer = DepartmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)




class Student(APIView):
    def Get(self,request):
        objs = Student.objects.all()
        serializer = StudentSerializer(objs, many=True)
        return Response(serializer.data)

    def Post(self,request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)

    def Get_by_id(self,request,id):
        objs = Student.objects.filter(id=id)
        serializer = StudentSerializer(objs, many=True)
        return Response(serializer.data)


class Nodue(APIView):
    def Get(self,request):
        objs = Nodue.objects.all()
        serializer = StudentSerializer(objs, many=True)
        return Response(serializer.data)

    def Post(self,request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)



