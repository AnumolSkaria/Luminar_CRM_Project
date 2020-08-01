
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from Enquiry.models import Course, Batch, Enquiry, Admission, Payment



class AddCourseForm(ModelForm):
    class Meta:
        model=Course
        fields=["Course"]
        widgets={
            'Course': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        pass

class UpdateCourseForm(ModelForm):
    class Meta:
        model=Course
        fields=["Course"]
        widgets={
            'Course': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        print("inside clean")

class AddBatchForm(ModelForm):
    class Meta:
        model=Batch
        fields=["Batch","Course","Date","Status"]
        widgets={
            'Batch': forms.TextInput(attrs={'class': 'form-control'}),
            'Date':forms.DateInput(attrs={'class':'form-control','type': 'date'}),
        }

    def clean(self):
        pass

class UpdateBatchForm(ModelForm):
    class Meta:
        model=Batch
        fields=["Batch","Course","Date","Status"]
        widgets = {
            'Batch': forms.TextInput(attrs={'class': 'form-control'}),
            'Date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }

    def clean(self):
        pass


class EnquiryForm(ModelForm):
    class Meta:
        model=Enquiry
        fields=["Student_name","Address","Qualification","College","Course","Batch","Contact","Email","Followup_date","Counceller","Source","Status"]
        widgets = {
            'Followup_date': forms.DateInput(attrs={'type': 'date'}),
            'Student_name':forms.TextInput(attrs={'class':'form-control'}),
            'Address':forms.Textarea(),
            'Qualification':forms.TextInput(attrs={'class':'form-control'}),
            'College':forms.TextInput(attrs={'class':'form-control'}),
            # 'Course':forms.ModelChoiceField(queryset=None,empty_label="(Nothing)"),
            'Contact':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            # 'Status':forms.TextInput(attrs={'class':'form-control'})
        }
    def clean(self):
        # print("inside clean")
        pass

class UpdateEnquiryForm(ModelForm):
    class Meta:
        model=Enquiry
        fields=["Student_name","Address","Qualification","College","Course","Batch","Contact","Email","Followup_date","Counceller","Source","Status"]
        widgets = {
            'Followup_date': forms.DateInput(attrs={'type': 'date'}),
            'Student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Address': forms.Textarea(),
            'Qualification': forms.TextInput(attrs={'class': 'form-control'}),
            'College': forms.TextInput(attrs={'class': 'form-control'}),
            # 'Course':forms.ModelChoiceField(queryset=None,empty_label="(Nothing)"),
            'Contact': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'Status':forms.TextInput(attrs={'class':'form-control'})
        }
    def clean(self):
        # print("inside clean")
        pass

class AdmissionForm(ModelForm):
    class Meta:
        model=Admission
        fields=["Admission_no","Enquiry_id","Course_fee","Batch"]
        # exclude=['Date']

    def clean(self):
        print("inside clean")

class PaymentForm(ModelForm):
    class Meta:
        model=Payment
        exclude=['Payment_date']

    def clean(self):
        pass

class StudentPaymentForm(ModelForm):
    class Meta:
        model=Payment
        fields=['Admission_no']
    def clean(self):
        print("inside clean")


class FollowupSearchForm(ModelForm):
    class Meta:
        model=Enquiry
        fields=["Followup_date"]
        labels={
            'Followup_date':"From"
        }
        widgets={
            'Followup_date':forms.DateInput(attrs={'type':'date'})
        }

    def clean(self):
        print('inside clean')
        cleaned_data=super().clean()
        dte=cleaned_data.get('Followup_date')
        qs=Enquiry.objects.filter(Followup_date=dte,Status='1')
        if(qs):
            print("found")
        else:
            msg="No followups on selected date"
            self.add_error('Followup_date',msg)
            print('error')

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email",'password1','password2']


class ReportBatchForm(ModelForm):
    class Meta:
        model=Batch
        fields=["Batch"]
        # widgets = {
        #     'Batch': forms.ModelChoiceField(queryset=Batch.objects.all())
        # }

    def clean(self):
        pass