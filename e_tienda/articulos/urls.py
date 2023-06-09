from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from articulos import views

urlpatterns = [
    path('', views.catalogo_articulos, name='catalogo_articulos'),
    path('articulos', views.lista_articulos, name='lista_articulos'),
    path('agregar', views.agregar_articulo, name='agregar_articulo'),
    path('editar/<int:id>', views.editar_articulo, name='editar_articulo'),
    path('eliminar/<int:id>', views.eliminar_articulo, name='eliminar_articulo'),
    path('resenas/<int:id>', views.VerResenas, name='ver_resenas'),
    path('agregar_resena/<int:id>', views.AgregarResena, name='agregar_resena'),
    path('editar_resena/<int:id>', views.EditarResena, name='editar_resena'),
    path('eliminar_resena/<int:id>', views.EliminarResena, name='eliminar_resena'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
