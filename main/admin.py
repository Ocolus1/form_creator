from django.contrib import admin
from .models import *
from django import forms
from django.forms import CheckboxSelectMultiple


class FormItemAdmin(admin.ModelAdmin):
    list_display = ("id", "form")
    list_display_links = ("id", "form")

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


# Register your models here.
admin.site.register(Field)
admin.site.register(Form)
admin.site.register(FormItem,FormItemAdmin)