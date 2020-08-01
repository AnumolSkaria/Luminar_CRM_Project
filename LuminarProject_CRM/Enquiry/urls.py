from django.contrib import admin
from django.urls import path, include

from Enquiry.views import *

urlpatterns = [

path("index",index,name='index'),
path('home',InFO.as_view(),name='home'),
path('index1',index1,name='index1'),


path('reg',RegistrationPage.as_view(),name='reg'),
path('nav',navBar,name='nav'),

path('login',UserLogin.as_view(),name='login'),
path('logsout',logoutUser,name='logout'),

path('course',AddCourse.as_view(),name='addcourse'),
path('updatecourse/<int:pk>',UpdateCourse.as_view(),name='updatecourse'),
path('deletecourse/<int:pk>',DeleteCourse.as_view(),name='deletecourse'),
path('listcourse',CourseList.as_view(),name='listcourse'),

path('batch',AddBatch.as_view(),name='addbatch'),
path('deletebatch/<int:pk>',DeleteBatch.as_view(),name='deletebatch'),
path('updatebatch/<int:pk>',BatchUpdate.as_view(),name='updatebatch'),

path('enquiry',AddEnquiry.as_view(),name='addenquiry'),
path('listenquiry',EnquiryList.as_view(),name='listenquiry'),
path('viewenquiry/<str:pk>',ViewEnquiry.as_view(),name='viewenquiry'),
path('delateenquiry/<str:pk>',DeleteEnquiry.as_view(),name='deleteenquiry'),
path('updateenquiry/<str:pk>', UpdateEnquiry.as_view(), name='updateenquiry'),

path('followup/',FollowUp.as_view(),name='followup'),
path('followupdetails/<str:pk>',FollowUpDetails.as_view(),name='followupdetails'),
path('followupsearch',FollowUpSearch.as_view(),name='search'),


path('admission/<str:pk>',NewAdmission.as_view(),name='new'),
path('payments/<str:pk>',StudentPayment.as_view(),name='payment'),
path('studentpay',Payments.as_view(),name='pay'),

path('batchreport',BeginBatchReport.as_view(),name='batchrepoort'),
path('ongoingbatch',OnGoingBatchReport.as_view(),name='ongoing'),
path('concellerreport',CouncellerReport.as_view(),name='counceller'),
path('Sourcereport',SourceReport.as_view(),name='source'),




# path('demo',demoIndex,name='demo'),
]