import pic_script
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

from .forms import DB_Form
from .models import DB_Image

import io
from django.http import FileResponse


def index(request):
    db_image = DB_Image.objects.all()
    form = DB_Form(request.POST, request.FILES)
    return render(request, "index.html", context = {'form' : form, 'db_image' : db_image,})

def create(request):
    if request.method == "POST":
        form = DB_Form(request.POST, request.FILES,)
        if form.is_valid():
            db_image = form.save(commit=False)
            db_image.text = pic_script.res_pic(db_image.image)
            db_image.save()
            return HttpResponse("<ul>"
                                    "<li><a href='/static/writer.txt' download> скачать </a></tr>"
                                    "<li><a href='/'> на главную </a></tr>"
                                "</ul")
    return HttpResponseRedirect("/")

def gallery(request):
    db_image = DB_Image.objects.all()
    return render(request, "gallery.html", context={'db_image': db_image,})
