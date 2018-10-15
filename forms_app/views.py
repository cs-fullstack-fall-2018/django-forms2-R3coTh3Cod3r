from django.shortcuts import render, get_object_or_404, redirect
from .models import FormModel
from  .forms import ModelofForm
from django.utils import timezone


def index(request):
    form_list = FormModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'forms_app/index.html', context)

def edit(request):
    post = get_object_or_404(FormModel)
    if request.method == "POST":
        form=ModelofForm(request.POST, instance=post)
        if form.is_valid():
            post= form.save(commit=False)
            post.name= request.user
            post.dateCreated = timezone.now()
            post.save()
        return redirect('detail')

    else:
        form = ModelofForm(instance=post)

        return render(request, 'forms_app/edit.html', {'form' : form})

def detail(request):
    post = get_object_or_404(FormModel)
    return render(request, 'forms_app/dateentry.html', {'post' : post})


def newpost(request):

    if request.method == "POST":
        form = ModelofForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.name = request.user
            post.dateCreated = timezone.now()
            post.save()
            return redirect('detail')

        else:
            form = ModelofForm()
            return render(request, 'forms_app/edit.html', {'form': form})