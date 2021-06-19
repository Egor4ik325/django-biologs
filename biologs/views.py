from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BiologPost
from .forms import BiopostForm
from django.http import Http404

# Create your views here.

def home(request):
    return render(request, 'biologs/index.html')

def terminology(request):
    return render(request, 'biologs/terminology.html')

def boot(request):
    return render(request, 'biologs/boot.html')

def bioposts(request):
    biopost_objects = BiologPost.objects.order_by('date_posted')
    context = {'bioposts': biopost_objects}
    return render(request, 'biologs/bioposts.html', context)

@login_required
def biopost(request, biopost_id):
    biopost = BiologPost.objects.get(id=biopost_id)
    context = {'biopost': biopost}
    return render(request, 'biologs/biopost.html', context)

@login_required
def create_biopost(request):
    if request.method == 'GET':
        form = BiopostForm()
        context = {'form': form}
        return render(request, 'biologs/create_biopost.html', context)
    elif request.method == 'POST':
        form = BiopostForm(data=request.POST)
        if form.is_valid():
            created_biopost = form.save(commit=False)
            created_biopost.author = request.user
            created_biopost.save()
            return redirect('biologs:bioposts')
        else:
            context = {'form': form}
            return render(request, 'biologs/create_biopost.html', context)
    else:
        Http404

@login_required
def edit_biopost(request, biopost_id):
    biopost = BiologPost.objects.get(id=biopost_id)
    if biopost.author != request.user:
        raise Http404

    if request.method == 'GET':
        form = BiopostForm(instance=biopost)
        context = {'form': form, 'biopost': biopost}
        return render(request, 'biologs/edit_biopost.html', context)
    elif request.method == 'POST':
        form = BiopostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('biologs:bioposts')
        else:
            context = {'form': form, 'biopost': biopost}
            return render(request, 'biologs/edit_biopost.html', context)
    else:
        raise Http404

@login_required
def delete_biopost(request, biopost_id):
    biopost = BiologPost.objects.get(id=biopost_id)
    if biopost.author != request.user:
        raise Http404

    biopost.delete()
    return redirect('biologs:bioposts')
