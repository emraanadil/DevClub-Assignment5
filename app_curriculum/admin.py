from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Standard)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Comment)
admin.site.register(Reply)