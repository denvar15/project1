from django.contrib import admin
from .models import Question, Choice, Input

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Input)

# Register your models here.
