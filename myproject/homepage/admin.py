from django.contrib import admin
from . models import Staff, Students, Courses, Messages


# Register your models here.
admin.site.register(Students)
admin.site.register(Staff)
admin.site.register(Courses)
admin.site.register(Messages)
