from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", login_view, name="login"),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path("", home_view, name="home"),
    
    path("profile/", include('social.urls')),
    # path("memory/<int:user_id>/<int:mem_id>", memory_view, name="memory")

    path("memory/", include('memory.urls'))
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


