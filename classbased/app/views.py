from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.views.generic import CreateView, UpdateView,DeleteView,ListView
from .models import *


class Index(CreateView):
    model=Create
    form_class=CreateForm
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["objects"]=self.model.objects.all()
        return context
    

class update(UpdateView):
    model=Create
    template_name='update.html'
    success_url="/"
    fields={
        "title",
        "complete"
    }


class delete(DeleteView):
    model=Create
    success_url="/"
    template_name='delete.html'




