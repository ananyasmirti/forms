from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, SnippetForm
from django.views.generic import  DetailView

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            report = form.cleaned_data['report']
            lead = form.cleaned_data['lead']
            hours = form.cleaned_data['hours']
            body = form.cleaned_data['body']
            progfile = form.cleaned_data['progfile']
            concern = form.cleaned_data['concern']
            next_plan = form.cleaned_data['next_plan']
            planfile = form.cleaned_data['planfile']
            print(name)
          

    else:
        form = ContactForm()

    return render(request, 'form/form.html', {'form':form})


def snippet_detail(request):

    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()


    form = SnippetForm()
    return render(request, 'form/form.html', {'form': form})

class Display(DetailView):
    form = SnippetForm()
    template_name = 'form/display.html'