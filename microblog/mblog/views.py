from django.shortcuts import render

from .models import MBlog
from .forms import UpdateMBForm

# Create your views here.

def home(request) : 
    mblogs = MBlog.objects.all()
    return render(request, 'home.html', \
        {'form' : UpdateMBForm, \
        'microblogs': mblogs})
