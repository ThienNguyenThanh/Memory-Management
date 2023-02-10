from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from memory.models import Memory


# @login_required
def home_view(request):
    search_q = request.GET.get('q')
    memory_queryset = None
    if(search_q is not None):
        memory_queryset = Memory.objects.filter(location__contains=search_q).values()
    else:
        memory_queryset = Memory.objects.all()
    context = {
        'memory_list': memory_queryset
    }

    return render(request, 'memory/home.html', context=context)

def memory_detail_view(request, user_id=None, mem_id=None):
    memory_obj = None
    if(mem_id):
        memory_obj = Memory.objects.get(id=mem_id)

    context = {
        'obj': memory_obj
    }

    return render(request, 'memory/memory.html', context=context)

