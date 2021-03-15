from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UploadImageForm


def index_form(request):
    print('hello waweqwe')
    context = {
        'form': UploadImageForm(None)
    }
    template_name = 'meta_picture/index.html'
    return render(request, template_name, context)


def index_action_form(request):
    print('hello world')
    print(request.FILES)
    form = UploadImageForm(request.POST, request.FILES)
    print()
    if form.is_valid():
        print('is valid')
        form.save()
    else:
        print('ERROR')
        print(form.errors)
    return HttpResponseRedirect('/')
