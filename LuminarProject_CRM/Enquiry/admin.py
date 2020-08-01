from django.contrib import admin

# Register your models here.
from Enquiry.models import Course, Batch, Enquiry, Admission, Payment, Counceller, Source

admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(Enquiry)
admin.site.register(Admission)
admin.site.register(Payment)
admin.site.register(Counceller)
admin.site.register(Source)