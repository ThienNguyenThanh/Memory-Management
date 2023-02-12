from django.urls import path
from .views import memory_detail_view, create_memory_view, map_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("<int:mem_id>", memory_detail_view, name="memory"),
    path("create", create_memory_view, name="creat_memory"),
    path("map", map_view, name="map")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)