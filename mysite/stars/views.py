from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from stars.models import Star, Type

# Create your views here.
class StarList(LoginRequiredMixin, View):
    def get(self, request):
        type = Type.objects.all().count()
        all = Star.objects.all()
        ctx = {'type_count': type, 'star_list': all}
        return render(request, 'stars/star_list.html', ctx)

class TypeView(LoginRequiredMixin, View):
    def get(self, request):
        type = Type.objects.all()
        ctx = {'type_list': type}
        return render(request, 'stars/type_list.html', ctx)

class TypeCreate(LoginRequiredMixin, CreateView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('stars:all')

class TypeUpdate(LoginRequiredMixin, UpdateView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('stars:all')

class TypeDelete(LoginRequiredMixin, DeleteView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('stars:all')

class StarCreate(LoginRequiredMixin, CreateView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars:all')

class StarUpdate(LoginRequiredMixin, UpdateView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars:all')

class StarDelete(LoginRequiredMixin, DeleteView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars:all')
