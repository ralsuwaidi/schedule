from django.shortcuts import render, redirect
from .forms import EventForm, POCForm, OrganizationForm, PermitForm
from django.contrib import messages
from .models import EventModel, PermitModel

# Create your views here.
def event_create_view(request):

    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        form2 = POCForm(request.POST)
        form3 = EventForm(request.POST, request.FILES)
        form4 = PermitForm(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():

            event = EventModel(**dict(**form.cleaned_data, **form2.cleaned_data, **form3.cleaned_data))
            event.save()

            permit = form4.save(commit=False)
            print(permit)
            print(event)
            permit.event = event
            permit.save()

            return render(request, 'events/success.html')
        else:
            return render(request, 'events/create.html', {'form': form, 'form2': form2, 'form3': form3, 'form4': form4})

    form = OrganizationForm()
    form2 = POCForm()
    form3 = EventForm()
    form4 = PermitForm()
    context = {
        'form': form, 
        'form2': form2,
        'form3': form3,
        'form4': form4,
    }
    return render(request, 'events/create.html', context=context)
