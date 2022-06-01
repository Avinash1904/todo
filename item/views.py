from datetime import datetime
from urllib import request
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator
from item.forms import ItemCreateForm, ItemUpdateForm
from item.models import Item
from item.permissions import is_task_creator
from django.contrib.auth.mixins import LoginRequiredMixin


class ItemsListView(LoginRequiredMixin, generic.ListView):
    model = Item
    paginate_by= 8

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class ItemDetailView(LoginRequiredMixin, generic.DetailView):
    model = Item

    def get_object(self, queryset=None):
        obj = super().get_object()
        if self.request.user != obj.user:
            raise Http404()
        return obj


class ItemCreateView(generic.edit.CreateView):
    model = Item
    form_class = ItemCreateForm

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(*args, **kwargs)
        initial['user'] = self.request.user
        initial['scheduled_at'] = datetime.now()
        return initial


class ItemUpdateView(generic.edit.UpdateView):
    model = Item
    # fields = ('name', 'description', 'scheduled_at', 'completed')
    form_class = ItemUpdateForm
    template_name = 'item/item_update.html'

    def get_object(self, queryset=None):
        obj = super().get_object()
        if self.request.user != obj.user:
            raise Http404()
        return obj



class ItemDeleteView(generic.DeleteView):
    model = Item
    success_url = reverse_lazy('items')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if self.request.user != obj.user:
            raise Http404()
        return obj
