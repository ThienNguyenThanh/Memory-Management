import json

import folium
import geocoder
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.shortcuts import redirect, render

from memory.models import Images, Memory

from .utils import get_img, resize_img, upload_img


@login_required
def map_view(request):
    form = None
    location = None

    # Create Map Object
    m = folium.Map(location=[0, 0], zoom_start=2)

    address = request.GET.get('q', None)
    if(address):

        location = geocoder.osm(address)
        lat = location.lat
        lng = location.lng
        country = location.country
        if (lat == None or lng == None):
            # address.delete()
            return HttpResponse('You address input is invalid')

        folium.Marker([lat, lng], tooltip='Click for more',
                  popup=country).add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
        'form': form,
        'location': location.address if location else '', 
        'location_details': json.dumps(location.json) if location else ''
    }
    return render(request, 'memory/map.html', context)

@login_required
def create_memory_view(request):
    location = request.GET.get('map', None)
    if location:
        location_JSON = json.loads(location)

    if(request.method == 'POST'):
        images = request.FILES.getlist('images_upload')

        location = location_JSON
        memory = Memory.objects.create(
                user = request.user,
                location = location_JSON.get('address'),
                lat = location_JSON.get('lat'),
                lng = location_JSON.get('lng'),
                comment = request.POST.get('comment'),
                visited_at = request.POST.get('visited_date')
            )
        for img in images:
            # Upload to Fisebase
            default_storage.save(img.name, img)
            resize_img(img.name)
            upload_img(request.user.id, memory.id, img.name)
            default_storage.delete(img.name)
            Images.objects.create(
                memory_id = memory,
                img_url = get_img(request.user.id, memory.id, img.name)
            )

        return redirect('/')
    context = {
        'address': location_JSON.get('address'),
    }

    return render(request, 'memory/create_memory.html', context=context)

@login_required
def memory_detail_view(request, user_id=None, mem_id=None):
    memory_obj = None
    if(mem_id):
        memory_obj = Memory.objects.get(id=mem_id)
        imgs = Images.objects.filter(memory_id=mem_id).values()
        
        carousel_item_active = None
        carousel_item = []
        for img in imgs:
            if(carousel_item_active is None):
                carousel_item_active = img.get('img_url')
            else:
                carousel_item.append(img.get('img_url'))
        
    context = {
        'obj': memory_obj,
        'carousel_active': carousel_item_active,
        'carousel': carousel_item
    }

    return render(request, 'memory/memory.html', context=context)

