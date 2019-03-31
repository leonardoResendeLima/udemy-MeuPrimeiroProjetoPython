from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm


# Create your views here.

def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'persons.html', {'persons': persons})


def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('persons_list')
    return render(request, 'person_new.html', {'form': form})


def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('persons_list')
    return render(request, 'person_new.html', {'form': form})

def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if request.method == "POST":
        person.delete()
        return redirect('persons_list')
    return render(request, 'person_delete_confirm.html', {'person' : person})

