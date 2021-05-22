from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Field, Form, FormItem
from .forms import FieldForm, FormItemForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    context = {}
    return render(request, 'main/index.html', context)


@login_required
def home(request):
    form = FieldForm(request.POST or None)
    fields = Field.objects.filter(user=request.user)
    order, created = Form.objects.get_or_create(user=request.user)
    if request.method == "POST":
        if form.is_valid:
            form.instance.user = request.user
            form.save()
            return redirect('home')
    context = {
        'form': form,
        'fields': fields,
        'order': order
    }
    return render(request, 'main/home.html', context)


@login_required
def create_form(request):
    form = FormItemForm(request.POST or None, request.user)
    order, created = Form.objects.get_or_create(user=request.user)
    if request.method == "POST":
        if form.is_valid:
            form.instance.form = order
            form.save()
            return redirect('preview')

    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)


@login_required
def preview(request):
    order, created = Form.objects.get_or_create(user=request.user)
    item = order.formitem_set.all().last()
    
    context = {
        'orders': item,
        'order': order
    }
    return render(request, 'main/preview.html', context)

@login_required
def del_field(request, id):
    field = Field.objects.get(pk=id)
    field.delete()
    return redirect('home')

def floor_temp(request, short_url):
    order = Form.objects.get(short_url=short_url)
    order.visits += 1
    order.save()
    item = order.formitem_set.all().last()
    if request.method == "POST":
        data = request.POST
        datas = {}
        for k,v in data.items():
            datas[k] = v

        datas.pop('csrfmiddlewaretoken')

        return JsonResponse(datas, safe=False)
        

    context = {
        'order': order,
        'item': item
    }

    return render(request, 'main/floor.html', context)
