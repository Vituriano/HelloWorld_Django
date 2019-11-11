from django.shortcuts import render
from django.views import generic
from .models import Gostos, Bio
# Create your views here.


class HomeView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Gostos'] = Gostos.objects.all()
        context['Bio'] = Bio.objects.all()
        return context
