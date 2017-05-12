from django.shortcuts import render

from .models import MBlog
from .forms import UpdateMBForm

# Create your views here.

def home(request) : 
    form = UpdateMBForm(request.POST)
    # if form.is_valid : 
        #mblog = MBlog.objects.get_or_create(content=request.POST.get('content'))

    mblogs = MBlog.objects.all()
    return render(request, 'home.html', \
        {'form' : UpdateMBForm, \
        'microblogs': mblogs})
