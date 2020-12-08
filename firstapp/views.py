import pic_script
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import DB_Form
from .models import DB_Image


def index(request):
    db_image = DB_Image.objects.all()
    form = DB_Form(request.POST, request.FILES)
    return render(request, "index.html", context = {'form' : form, 'db_image' : db_image, 'script' : pic_script.res_pic ('media/images/cold_war_wallpaper.jpg')})

def create(request):
    if request.method == "POST":
        form = DB_Form(request.POST, request.FILES,)
        if form.is_valid():
            db_image = form.save(commit=False)
            db_image.text = pic_script.res_pic(db_image.image)
            db_image.save()
    return HttpResponseRedirect("/")

def gallery(request):
    db_image = DB_Image.objects.all()
    return render(request, "gallery.html", context={'db_image': db_image,})
