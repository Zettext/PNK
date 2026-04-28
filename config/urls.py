from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from galeria import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # Esto activa login/logout
    path('', views.index, name='index'),
    path('eliminar/<int:foto_id>/', views.eliminar_foto, name='eliminar_foto'),
]

# Esto es vital para poder ver las imágenes en modo local
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)