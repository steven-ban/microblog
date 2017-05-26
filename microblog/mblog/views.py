from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import MBlog
from .forms import UpdateMBForm

# Create your views here.

def home(request) : 
    if request.method == 'POST' : 
        form = UpdateMBForm(request.POST)
        if form.is_valid : 
            mblog = form.save()
            mblog.save()
            return render(request, 'home.html', {'form' : UpdateMBForm, \
        'microblogs': mblogs})

    mblogs = MBlog.objects.order_by('-time')[0:3]
    return render(request, 'home.html', \
        {'form' : UpdateMBForm, \
        'microblogs': mblogs})
