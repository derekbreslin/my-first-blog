from django.shortcuts import render
from django.views.generic.edit import CreateView

from ggg.forms import EntrygggForm

class AddGggEntryView(CreateView):
    # model - entryggg
    form_class = EntrygggForm
    template_name = 'new.html'
    success_url = '/home/'

# Create your views here.
def gggtournament(response):
    return render(response, "ggg/gggtournament.html", {})

def new_entry(request):
    form = EntrygggForm()
    return render(request, 'ggg/new.html', {'form': form})

def testtournament(response):
    return render(response, "ggg/testtournament.html", {})
    