from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .forms import UploadImageForm
from .models import *
from .services import *


def index_form(request):
    context = {
        'images': Image.objects.all(),
        'form': UploadImageForm(None)
    }
    return render(request, 'meta_picture/index.html', context)


def index_action_form(request):
    for filename, file in request.FILES.items():
        f_name = request.FILES[filename].name
    form = UploadImageForm(request.POST, request.FILES)
    if form.is_valid():
        new_image = form.save(commit=False)
        new_image.title = form.cleaned_data['title']
        new_image.slug = set_default_slug(new_image.title)
        new_image.save()

    create_meta_data(f_name, new_image.slug)

    return HttpResponseRedirect('/')


def detail_photo(request, slug):
    image = Image.objects.get(slug=slug)
    context = {
        'image': image,
        'meta_data': ImageMetaData.objects.get(image=image),
        'hex_color': rgb2hex(
            ImageMetaData.objects.get(image=image).average_color
        )
    }
    return render(request, 'meta_picture/detail_photo.html', context)