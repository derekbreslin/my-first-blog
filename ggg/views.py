
from django.shortcuts import render
from django.views.generic.edit import CreateView

from ggg.forms import EntrygggForm
from django.contrib import messages

class AddGggEntryView(CreateView):
    # model - entryggg
    form_class = EntrygggForm
    template_name = 'new.html'
    success_url = '/home/'


    def __str__(self):
        return self.Name

    def new_ggg_entry(request):        
        ggg_entry_form = EntrygggForm()
        template_name = 'gggtournament/new.html'
        return render(request, template_name)


#        return render(request, 'ggg/new.html', {'form': ggg_entry_form})
#    if request.method == 'POST':
#        ggg_entry_form = EntrygggForm(request.POST)
#        # Do Something
#        if ggg_entry_form.is_valid():
#            ggg_entry_form.save()
#            messages.success(request, ('Your prediction was saved - good luck!'))
#        else:
#            messages.error(request, 'Your form could not be saved')
 


# Create your views here.
def gggtournament(request):
    return render(request, "ggg/gggtournament.html", {})

def testtournament(request):
    return render(request, "ggg/testtournament.html", {})

def new_entry(request):
    form = EntrygggForm()
    return render(request, 'ggg/new.html', {'form': form})

def create(request):
    if request.method == "POST":
        form = EntrygggForm(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = EntrygggForm(name=n)
            t.save()

        return render(request, "ggg/gggtournament/new.html", {"form":form})
    else:
        form = EntrygggForm()

    return render(request, "ggg/gggtournament/new.html", {"form":form})