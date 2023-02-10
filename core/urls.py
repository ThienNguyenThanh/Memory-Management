from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
# from social import views
from memory.views import home_view, memory_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("login/", views.login, name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # path('oauth/', include('social_django.urls', namespace="social")),
    path("", home_view, name="home"),
    # path("memory/<int:user_id>/<int:mem_id>", memory_view, name="memory")
    path("memory/<int:mem_id>", memory_detail_view, name="memory")
]
