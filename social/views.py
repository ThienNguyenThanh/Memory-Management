import json

import folium
import geocoder
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from memory.models import Memory


@login_required
def profile_view(request):
    form = None

    # Create Map Object
    m = folium.Map(location=[0, 0], zoom_start=2)

    user_mem = Memory.objects.filter(user=request.user)
    for mem in user_mem:
        folium.Marker([mem.lat, mem.lng], tooltip='Click for more',
                  popup=mem.location).add_to(m)
                  
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m
    }
    return render(request, 'social/profile.html', context)


