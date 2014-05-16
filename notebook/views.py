from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import TextNote

def homepage(request):
    return HttpResponse('<html><title>mac</title></html>')

class Homepage(ListView):
    queryset = TextNote.objects.filter(is_published=True).order_by('pub_date')
    template_name = 'notebook/home.html'
    context_object_name = 'latest_published_textnotes'
