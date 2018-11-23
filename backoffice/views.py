from django.shortcuts import render, redirect

# Create your views here.
from backoffice.forms import CrudForm
from backoffice.models import Crud


def index(request):
    ctx = {}
    return render(request, 'index.html', ctx)


def listCrud(request):
    ctx = {'object_list': Crud.objects.all()}
    return render(request, 'crud/list.html', ctx)


def addCrud(request):
    if request.method == 'POST':
        form = CrudForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('list-crud')

    ctx = {'form': CrudForm()}
    return render(request, 'crud/add.html', ctx)


def detailCrud(request, pk):
    crud = Crud.objects.get(pk=pk)
    ctx = {'object': crud}

    return render(request, 'crud/detail.html', ctx)


def editCrud(request, pk):
    crud = Crud.objects.get(pk=pk)
    if request.method == 'POST':
        form = CrudForm(request.POST, instance=crud)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('list-crud')

    ctx = {'form': CrudForm(instance=crud)}
    return render(request, 'crud/edit.html', ctx)


def deleteCrud(request, pk):
    crud = Crud.objects.get(pk=pk)
    if request.method == 'POST':
        crud.delete()
        return redirect('list-crud')

    ctx = {'object': crud}
    return render(request, 'crud/delete.html', ctx)



