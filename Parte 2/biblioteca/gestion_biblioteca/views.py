from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Libro, Revista, Prestamo
from django.db.models import Count

class HomePageView(TemplateView):
 template_name = 'pages/home.html'

# Las consultas sql solicitadas en formato ORM de Django
def listar_items_disponibles(request):
    items_prestados = Prestamo.objects.filter(fecha_devolucion__isnull=True).values_list('item_id', flat=True)
    items_disponibles = Libro.objects.exclude(id__in=items_prestados)

    context = {'items_disponibles': items_disponibles}
    return render(request, 'gestion_biblioteca/items_disponibles.html', context)

def listar_items_prestados(request):
    prestamos_activos = Prestamo.objects.filter(fecha_devolucion__isnull=True)

    context = {'prestamos_activos': prestamos_activos}
    return render(request, 'gestion_biblioteca/items_prestados.html', context)

def item_mas_prestado(request):
    item_mas_prestado = Prestamo.objects.values('item').annotate(total_prestamos=Count('item')).order_by('-total_prestamos').first()
    item = None
    if item_mas_prestado:
        item = Libro.objects.get(id=item_mas_prestado['item'])

    context = {
        'item_mas_prestado': item,
        'total_prestamos': item_mas_prestado['total_prestamos'] if item_mas_prestado else 0
    }
    return render(request, 'gestion_biblioteca/item_mas_prestado.html', context)
