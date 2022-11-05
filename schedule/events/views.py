from django.shortcuts import render
from .forms import EventForm

# Create your views here.
def event_create_view(request):

    if request.method == 'POST':
        print('form')
        form = EventForm(request.POST)
        if form.is_valid():
            print(form)
        else:
            form = EventForm()

        return render(request, 'events/create.html', {'form': form})

    form = EventForm()
    return render(request, 'events/create.html', {'form': form})
