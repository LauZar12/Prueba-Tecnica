from django.urls import path
from . import views
from .views import HomePageView, item_mas_prestado, listar_items_disponibles, listar_items_prestados

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('itemsdisponibles/', views.listar_items_disponibles, name='items_disponibles'),
    path('itemsprestados/', views.listar_items_prestados, name='items_prestados'),
    path('itemmasprestado/', views.item_mas_prestado, name='item_mas_prestado'),
]

