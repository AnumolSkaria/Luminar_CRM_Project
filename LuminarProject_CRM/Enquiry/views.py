

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Count, Sum
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.utils.datetime_safe import date, datetime
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView, UpdateView

from Enquiry.forms import AddCourseForm, AddBatchForm, EnquiryForm, UpdateEnquiryForm, UpdateBatchForm, \
    UpdateCourseForm, AdmissionForm, PaymentForm, FollowupSearchForm, StudentPaymentForm, CreateUserForm, \
    ReportBatchForm
from Enquiry.models import Course, Batch, Enquiry, Admission, Payment


class AddCourse(TemplateView):
    model=Course
    template_name = "Course/add_course.html"
    form_class=AddCourseForm

    def get(self, request, *args, **kwargs):
        form=self.form_class
        qs=Course.objects.all()
        context={}
        context["form"]=form
        context["course"]=qs
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addcourse')
        else:
            context = {}
            context["form"] = form
            return render(request,self.template_name,context)

class UpdateCourse(TemplateView):
    model=Course
    template_name = "Course/update_course.html"
    form_class=UpdateCourseForm
    def get(self, request, *args, **kwargs):
        id=self.kwargs.get('pk')
        qs=Course.objects.get(id=id)
        print(qs)
        form=self.form_class(instance=qs)
        context={}
        context['form']=form
        return render(request,self.template_name,context)
    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST)
        id = self.kwargs.get('pk')
        print(id)
        qs = Course.objects.filter(id=id)
        print(qs)
        if form.is_valid:
            print('ok')
            form.save()
            # print('ok')
            # print('inside')
            # cname=form.cleaned_data['Course']
            # qs.Course=cname
            # qs.save()
            return redirect('addcourse')

class DeleteCourse(TemplateView):
    model=Course
    def get(self, request, *args, **kwargs):
        c_id=self.kwargs.get('pk')
        qs=Course.objects.get(id=c_id).delete()
        context={}
        context["form"]=qs
        return redirect("addcourse")

class CourseList(ListView):
    model = Course
    template_name = 'Course/list_course.html'
    context_object_name = "qs"



class AddBatch(TemplateView):
    model=Batch
    template_name = "Batch/add_batch.html"
    form_class=AddBatchForm

    def get(self, request, *args, **kwargs):
        form=self.form_class
        qs=Batch.objects.all()
        context={}
        context["form"]=form
        context["Batch"]=qs
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addbatch')
        else:
            context = {}
            context["form"] = form
            return render(request,self.template_name,context)


class DeleteBatch(TemplateView):
    model=Batch
    def get(self, request, *args, **kwargs):
        b_id=self.kwargs.get('pk')
        qs=Batch.objects.get(id=b_id).delete()
        context={}
        context["form"]=qs
        return redirect("addbatch")
# class Home(TemplateView):
#     template_name = "index/home.html"


class BatchUpdate(TemplateView):
    model=Batch
    template_name = 'Batch/update_batch.html'
    form_class=UpdateBatchForm
    def get(self, request, *args, **kwargs):
        b_id=self.kwargs.get('pk')
        qs=Batch.objects.get(id=b_id)
        form=self.form_class(instance=qs)
        context={}
        context['form']=form
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        b_id = self.kwargs.get('pk')
        qs = Batch.objects.get(id=b_id)
        if form.is_valid():
            bname=form.cleaned_data['Batch']
            bcourse=form.cleaned_data['Course']
            bdate=form.cleaned_data['Date']
            bstatus=form.cleaned_data['Status']
            print(bname)
            qs.Batch=bname
            qs.Course=bcourse
            qs.Date=bdate
            qs.Status=bstatus
            qs.save()
            return redirect('addbatch')
        else:
            form=self.form_class(request.POST)
            context={}
            context['form']=form
            return render(request,self.template_name,context)

def Home(request):
    return render(request,'index/home.html')
# def Home(request):
#     return render(request,'theme/index.html')




class AddEnquiry(CreateView):
    model = Enquiry
    form_class=EnquiryForm
    template_name = 'Enquiry/add_enquiry.html'
    success_url = reverse_lazy('listenquiry')


class EnquiryList(ListView):
    model=Enquiry
    template_name = 'Enquiry/list_enquiry.html'
    context_object_name = "qs"

class ViewEnquiry(DetailView):
    model = Enquiry
    template_name = 'Enquiry/view_enquiry.html'
    context_object_name = "details"

class DeleteEnquiry(DeleteView):
    model = Enquiry
    template_name = 'Enquiry/delete_enquiry.html'
    success_url = reverse_lazy('listenquiry')

class UpdateEnquiry(UpdateView):
    model = Enquiry
    template_name = 'Enquiry/update_enquiry.html'
    form_class = UpdateEnquiryForm
    success_url = reverse_lazy('listenquiry')

class FollowUp(TemplateView):
    model=Enquiry
    template_name = 'Enquiry/enquiry_followup.html'
    def get_queryset(self):
        return Enquiry.objects.filter(Followup_date=date.today(),Status='1')
    def get(self, request, *args, **kwargs):
        context={}
        context["followup"]=self.get_queryset()
        return render(request,self.template_name,context)


class FollowUpDetails(UpdateView):
    model = Enquiry
    template_name = "Enquiry/followup_details.html"
    form_class = UpdateEnquiryForm
    def get(self, request, *args, **kwargs):
        id=self.kwargs.get('pk')
        qs=Enquiry.objects.get(Enquiry_id=id)
        form=self.form_class(instance=qs)
        context={}
        context['form']=form
        context['id']=id
        return render(request,self.template_name,context)
# class AllFollowup(TemplateView):
#     model=Enquiry
#     template_name = "Enquiry/all_followups.html"
#     def get(self, request, *args, **kwargs):
#         qs=Enquiry.objects.filter(Followup_date=date.year)
#         context={}
#         context['form']=qs
#         return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        qs = Enquiry.objects.get(Enquiry_id=id)
        form = self.form_class(request.POST,instance=qs)
        if form.is_valid():
            form.save()
            return redirect('followup')


class FollowUpSearch(TemplateView):
    model=Enquiry
    template_name = "Enquiry/followup_search.html"
    form_class=FollowupSearchForm
    def get(self, request, *args, **kwargs):
        form=self.form_class
        context={}
        context['form']=form
        return render(request,self.template_name,context)
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            dte=form.cleaned_data['Followup_date']
            # edte=dte+datetime.timedelta(days=1)
            # edte=dte+datetime.date(datetime.today())
            print(dte)
            qs=Enquiry.objects.filter(Followup_date=dte,Status='1')
            # qs = Enquiry.objects.filter(some_datetime_field__range=[dte,edte])
            print(qs)
            if(qs):
                context={}
                context['item']=qs
                template_name="Enquiry/followupsearch_list.html"
                return render(request,template_name,context)
        else:
            form=self.form_class(request.POST)
            context={}
            context['form']=form
            return render(request,self.template_name,context)

class NewAdmission(TemplateView):
    model=Admission
    template_name = "Admission/new_admission.html"
    form_class=AdmissionForm
    def get(self, request, *args, **kwargs):
        id=self.kwargs.get('pk')
        form=self.form_class(initial={'Enquiry_id':id})
        context={}
        context['form']=form
        return render(request,self.template_name,context)
    def post(self,request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            id=self.kwargs.get('pk')
            qs=Enquiry.objects.get(Enquiry_id=id)
            qs.Status='2'
            qs.save()
            admission_no=form.cleaned_data['Admission_no']
            form.save()
            return redirect('payment',pk=admission_no)
            # return StudentPayment.as_view()(self.request,*args,**kwargs)
        else:
            form=self.form_class(request.POST)
            context={}
            context['form']=form
            return render(request,self.template_name,context)

class StudentPayment(TemplateView):
    model=Payment
    template_name = 'Admission/ayment.html'
    form_class=PaymentForm
    def get(self, request, *args, **kwargs):
        id=self.kwargs.get('pk')
        qs=Admission.objects.get(Admission_no=id)
        qs4 = Payment.objects.filter(Admission_no=id)
        # print(qs)
        # print(qs4)
        enqid=qs.Enquiry_id
        fee=qs.Course_fee
        # print(fee)
        qs1=Enquiry.objects.get(Enquiry_id=enqid)
        from django.db.models import Sum
        qs2=Payment.objects.filter(Admission_no=id).values('Amount').annotate(remaining=Sum('Amount'))
        if(qs2):
            print('ok')
            remaining=fee-(qs2[0]['remaining'])
        else:
            remaining=fee
        print(remaining)
        form=self.form_class(initial={'Admission_no':id,'Enquiry_id':enqid})
        context={}
        context['form']=form
        context['pay']=qs1
        context['detail']=qs4
        context['remaining']=remaining
        return render(request,self.template_name,context)
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form=self.form_class(request.POST)
            context={}
            context['form']=form
            return render(request,self.template_name,context)

class Payments(TemplateView):
    model=Payment
    template_name = 'Admission/student_payment.html'
    form_class=StudentPaymentForm
    def get(self, request, *args, **kwargs):
        form=self.form_class
        context={}
        context['form']=form
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            id=form.cleaned_data['Admission_no']
            # form.save()
            return redirect('payment',pk=id)

        else:
            form=self.form_class(request.POST)
            context={}
            context['form']=form
            return render(request,self.template_name,context)

class InFO(TemplateView):
    model=Enquiry
    template_name = 'index/home.html'
    def get(self, request, *args, **kwargs):
        from django.db.models import Count
        qs=Enquiry.objects.filter(Batch__Status='1').values('Batch__Batch','Batch__Course__Course','Batch__Date').annotate(enqcount=(Count('Enquiry_id')))
        # print(qs)
        qs1=Admission.objects.all().values('Batch__Batch','Batch__Course__Course').annotate(enq=(Count('Admission_no')))
        # print(qs1)
        # print(qs)
        context={}
        context["qs"]=qs
        context['qs1']=qs1


        return render(request,self.template_name,context)

class BeginBatchReport(TemplateView):
    model=Enquiry
    template_name = 'Report/batch_report.html'
    def get(self, request, *args, **kwargs):
        qs1 = Admission.objects.filter(Batch__Status='1').values('Batch__Batch', 'Batch__Course__Course', 'Batch__Date').annotate(student=(Count('Admission_no')), coursefee=(Sum('Course_fee')))
        # qs = Payment.objects.filter(Enquiry_id__Batch__Status='1').values('Amount').annotate(paid=(Sum('Amount')))
        context={}
        context['form']=qs1
        return render(request,self.template_name,context)

class OnGoingBatchReport(TemplateView):
    model=Enquiry
    template_name = 'Report/ongoingbatch_report.html'
    def get(self, request, *args, **kwargs):
        qs1 = Admission.objects.filter(Batch__Status='2').values('Batch__Batch', 'Batch__Course__Course', 'Batch__Date').annotate(student=(Count('Admission_no')), coursefee=(Sum('Course_fee')))
        # qs = Payment.objects.filter(Enquiry_id__Batch__Status='1').values('Amount').annotate(paid=(Sum('Amount')))
        # print(qs1)
        context={}
        context['form']=qs1
        return render(request,self.template_name,context)



class CouncellerReport(TemplateView):
    model=Enquiry
    template_name = 'Report/counceller_report.html'
    def get(self, request, *args, **kwargs):
        qs=Enquiry.objects.all().values('Counceller__Counceller_name','Batch__Batch','Batch__Course__Course').annotate(studentno=(Count('Counceller__Counceller_name')))
        # print(qs)
        context={}
        context['form']=qs
        return render(request,self.template_name,context)


class SourceReport(TemplateView):
    model=Enquiry
    template_name = 'Report/source_report.html'
    def get(self, request, *args, **kwargs):
        qs=Enquiry.objects.all().values('Source__Source','Batch__Batch','Batch__Course__Course').annotate(studentno=(Count('Source__Source')))
        # print(qs)
        context={}
        context['form']=qs
        return render(request,self.template_name,context)

class RegistrationPage(TemplateView):
    model=User
    template_name = 'index/registration.html'
    form_class=CreateUserForm()
    def get(self, request, *args, **kwargs):
        context={}
        context['form']=self.form_class
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):
        form=CreateUserForm(request.POST)
        if form.is_valid():
            print('ok')
            form.save()
            return redirect('login')
        else:
            context={}
            context['form']=self.form_class
            return render(request,self.template_name,context)


def index(request):
    return render(request,'index/index.html')


class UserLogin(TemplateView):
    model=User
    template_name = 'index/login.html'
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)

    def post(self, request, *args, **kwargs):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        # print(user)
        if user is not None:
            print('ok')
            login(request,user)
            context={}
            context['user']=user
            return redirect('home')
        else:
            message="incorrect Username or password"
            context={}
            context['message']=message
        return render(request,self.template_name,context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def navBar(request):
    return render(request,'index/navbar.html')

def index1(request):
    return render(request,'index/index1.html')