from django.db import models
from django.contrib.auth.models import User
import string
from random import choices


class Field(models.Model):
    name = models.CharField(max_length=100, null=True)
    types = models.CharField(max_length=20, null=True)
    ids = models.CharField(max_length=50, null=True)
    required = models.BooleanField(default=False, null=True, blank=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Form(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    short_url = models.CharField(max_length=100, unique=True, blank=True, null=True)
    visits = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.user)}" 

    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        if self.short_url:
            pass
        else:
            self.short_url = self.generate_short_link()

    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        short_url = "".join(choices(characters, k=6))

        link = Form.objects.filter(short_url=short_url)

        if link:
            return self.generate_short_link()

        return short_url
        

class FormItem(models.Model):
    field = models.ManyToManyField(Field)
    form = models.ForeignKey(Form, on_delete=models.SET_NULL, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.form.user} form {self.id}"




