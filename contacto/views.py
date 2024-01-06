from django.shortcuts import render , redirect
from .forms import Formulario
from django.core.mail import EmailMessage



#Create your views here.

def contacto(request):
    if request.method == "POST" :
        formulario_contacto = Formulario(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            mail = request.POST.get("mail")
            contenido = request.POST.get("contenido")
            
            email = EmailMessage(f"Mensaje desde Turismo.com","Nombre: {}\nEmail: {}\nMensaje:\n{}".format(nombre,mail,contenido),
                                "",["marianolaclau@gmail.com"])
            
            email.send()
            return redirect ("/contacto/?valido")
    else:
        formulario_contacto = Formulario()
                
    return render(request,"contacto.html",{"formulario":formulario_contacto})



