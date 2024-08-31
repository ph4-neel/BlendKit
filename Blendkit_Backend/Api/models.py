from django.db import models

# College Model

class College(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    address = models.TextField()

class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str :
        return self.department

    class Meta:
        ordering = ['department']


class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) ->str:
        return self.student_id

class Student(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100,null=True)
    mother_name = models.CharField(max_length=100,null=True)
    reg_no = models.CharField(null=True)
    phone = models.CharField(max_length=100)
    address = models.TextField()

    department = models.ForeignKey(Department,related_name="department",on_delete=models.CASCADE)
    student_id = models.ForeignKey(StudentID,related_name='student_id',on_delete=models.CASCADE)
    College = models.ForeignKey(College,on_delete=models.CASCADE)


class Nodue(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=100)
    reason = models.TextField()
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=70)

class FacultyID(models.Model):
    faculty_id = models.CharField(max_length=100)

    def __str__(self) ->str:
        return self.faculty_id


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    faculty_id = models.ForeignKey(FacultyID,related_name='faculty_id',on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name="department", on_delete=models.CASCADE)
    College = models.ForeignKey(College, on_delete=models.CASCADE)









