from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tienda.urls')),        # La raíz redirige a las URLs de la app "tienda"
    path('profile/', include('tienda.urls')), # URLs de la app "tu_app"
]
    