from django.shortcuts import render, redirect
from .forms import ImageForm
from django.core.files.storage import FileSystemStorage
from .models import Image
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.
def form(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect('home')
    form = ImageForm()
    form.user = request.user
    context = {
        'form': form,
    }
    return render(request, 'form.html', context=context)