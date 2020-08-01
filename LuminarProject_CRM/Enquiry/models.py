
import uuid
from datetime import date

from django.db import models

# Create your models here.
# from django.utils.datetime_safe import date


class Course(models.Model):
    Course=models.CharField(max_length=150,unique=True)

    def __str__(self):
        return self.Course

class Batch(models.Model):
    Batch=models.CharField(max_length=150,unique=True)
    Course=models.ForeignKey(Course,on_delete=models.CASCADE)
    Date = models.DateField()
    Action = (
        ('1', 'Yet to Begin'),
        ('2', 'Started'),
        ('3', 'Completed')
    )
    Status = models.CharField(max_length=100, choices=Action)

    def __str__(self):
        return self.Batch
class Counceller(models.Model):
    Counceller_name=models.CharField(max_length=150)
    Contact=models.IntegerField()

    def __str__(self):
        return self.Counceller_name

class Source(models.Model):
    Source=models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.Source

class Enquiry(models.Model):

    Enquiry_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    Student_name=models.CharField(max_length=200)
    Address=models.CharField(max_length=250)
    Qualification=models.CharField(max_length=50)
    College=models.CharField(max_length=150)
    Course=models.ForeignKey(Course,on_delete=models.CASCADE)
    Batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
    Contact=models.IntegerField()
    Email=models.EmailField()
    Enquiry_date=models.DateField(default=date.today())
    Followup_date=models.DateField()
    Counceller=models.ForeignKey(Counceller,on_delete=models.CASCADE)
    Source=models.ForeignKey(Source,on_delete=models.CASCADE)
    Action=(
            ('1','Call_Back'),
            ('2','Admitted'),
            ('3','Cancel')
    )
    Status=models.CharField(max_length=20,choices=Action)

    def __str__(self):
        return str(self.Enquiry_id)


class Admission(models.Model):
    Admission_no=models.CharField(max_length=100,unique=True)
    Enquiry_id=models.CharField(max_length=100)
    Course_fee=models.IntegerField()
    Batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
    Date=models.DateField(default=date.today())

    def __str__(self):
        return self.Admission_no

class Payment(models.Model):
    Admission_no=models.CharField(max_length=50)
    Amount=models.IntegerField()
    Payment_date=models.DateField(default=date.today())
    Enquiry_id=models.CharField(max_length=100)

    def __str__(self):
        return self.Admission_no
