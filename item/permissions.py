from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Item

def is_task_creator(function):
    def checker(request, *args, **kwargs):
        print("checking ...")
        user = request.user
        item = get_object_or_404(Item, pk=kwargs.get('pk'))
        if item.user != user:
            return HttpResponse('Please do not try to see other users tasks')
        return function
    return checker