from django import forms
from .models import DB_Image


class DB_Form(forms.ModelForm):
    class Meta:
        model = DB_Image
        fields = ("image",)#поле "file" - для пользоваетльского .txt файла
