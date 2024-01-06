from django.shortcuts import render , redirect
from carro.carro import Carro
from pedidos.models import LineaPedido , Pedido
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from tienda.models import Producto
# Create your views here.

def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    linea_pedidos = []
    total_pedido = 0
    for key , value in carro.carro.items():
        cantidad = value["cantidad"]
        user = request.user
        producto = Producto.objects.get(id=key)
        subtotal = producto.precio * cantidad
        total_pedido += subtotal
        linea_pedidos.append(LineaPedido(
            producto_id = key,
            cantidad = cantidad,
            user = user,
            pedido = pedido,
            subtotal = subtotal
            ))

    #Persistimos en la bd todas las instancias creadas con un solo metodo   
    LineaPedido.objects.bulk_create(linea_pedidos)
    
    enviar_email(
        pedido=pedido,
        linea_pedido = linea_pedidos,
        nombreusuario = request.user.username,
        emailusuario = request.user.email,
        total = total_pedido,
        subtotal = subtotal
    )
    
    request.session['pedido_realizado'] = True
    Carro.limpiar_carro(request)
    return redirect("Tienda")

#Creamos un metodo para enviar un email personalizado en formato html
def enviar_email(**kwargs):
    asunto = "Pedido realizado con exito."
    mensaje = render_to_string("pedidos.html",{
                            "pedido":kwargs.get("pedido"),
                            "linea_pedido":kwargs.get("linea_pedido"),
                            "nombreusuario":kwargs.get("nombreusuario"),
                            "email":kwargs.get("emailusuario"),
                            "total":kwargs.get("total"),
                            "subtotal":kwargs.get("subtotal")
                            })
    
    #Quitamos las etiquetas html al contenido del mensaje
    mensaje_texto = strip_tags(mensaje)
    
    from_email = "marianolaclau@hotmail.com"
    to= kwargs.get("emailusuario")

    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)

