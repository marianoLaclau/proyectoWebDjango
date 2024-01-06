from django.shortcuts import render
from .models import Producto, CategProductos

def tienda(request):
    pedido_realizado = request.session.get('pedido_realizado', False) #Usamos esta variable para enviar una alerta al concretar pedido
    
    categoria_id = request.GET.get('categoria_id')  # Obtener el parámetro de la URL
    
    carro = request.session.get('carro', {})
    total_productos = sum(item['cantidad'] for item in carro.values())
    request.session['pedido_realizado'] = False

    categorias = CategProductos.objects.all()
    productos = Producto.objects.all()

    if categoria_id:
        # Si hay una categoría seleccionada, filtrar los productos por esa categoría
        productos = Producto.objects.filter(categoria_id=categoria_id)

    #Luego de almacenar su valor lo dejamos en False para que no vuelva a aparecer
    request.session['pedido_realizado'] = False
    
    contexto = {
        'items': carro.items(),
        'total_productos': total_productos,
        'pedido_realizado': request.session.get('pedido_realizado', False),
        'categorias': categorias,
        'productos': productos,
        'categoria_id': int(categoria_id) if categoria_id else None,  # Convertir a entero si existe
        'pedido_realizado':pedido_realizado
    }

    return render(request, "tienda.html", context=contexto)







