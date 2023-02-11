from django.shortcuts import render, redirect
from memory.models import Memory
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

def login_view(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                "error": "Invalid username or password"
            }
            return render(request, 'login.html', context)

        login(request, user)
        return redirect('/')
    return render(request, 'login.html')

@login_required
def home_view(request):
    search_q = request.GET.get('q')
    memory_queryset = None
    if(search_q is not None):
        memory_queryset = Memory.objects.filter(location__contains=search_q).values()
    else:
        memory_queryset = Memory.objects.all()

    print(request.POST.get('username'))
    context = {
        'memory_list': memory_queryset
    }

    return render(request, 'home.html', context=context)