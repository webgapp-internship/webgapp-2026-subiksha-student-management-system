from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):

    list_display = ['name', 'email', 'password']

admin.site.register(Form, FormAdmin)