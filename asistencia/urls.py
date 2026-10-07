from django.urls import path
from . import views

urlpatterns = [
    path("crear/", views.crear),
    path("lista/", views.listar),
    path("detalle/<id>/", views.detalle),
    path("editar/<id>/",views.editar),
    path("eliminar/<id>/",views.eliminar)
]