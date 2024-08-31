from rest_framework import serializers
from .models import *



class CollegeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = College
        fields = "__all__"

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    college = CollegeSerializer()
    department = DepartmentSerializer()
    class Meta:
        model = Student
        fields = "__all__"

class NodueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nodue
        fields = "__all__"

class FacultySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faculty
        fields = "__all__"