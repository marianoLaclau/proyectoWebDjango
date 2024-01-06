from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.views.generic import View
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User

# Create your views here.


#Personaliza la clase de Django con atributos extra
class FormCustom(UserCreationForm):
    email = forms.EmailField(required=True, help_text=None)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username': None,
            'password1': 'Custom help text for password1.',
            'password2': 'Custom help text for password2.',
        }

    def __init__(self, *args, **kwargs):
        super(FormCustom, self).__init__(*args, **kwargs)


#Vista para registro
class VRegistro(View):

    def get(self,request):
        form = FormCustom()
        return render(request,"registro.html",{"form":form})
    

    def post(self,request):
        form = FormCustom(request.POST)
        
        if form.is_valid():
            usuario = form.save()
            login(request,usuario)
        
        else:
            for msj in form.error_messages:
                messages.error(request,form.error_messages[msj])
            return render(request,"registro.html",{"form":form})    
        
        
        return redirect("Home")


#Vistas para login
def cerrar_sesion(request):
    
    logout(request)

    return redirect("Home")    



def ingresar(request):

    if request.method == "POST" :
            form = AuthenticationForm(request,data=request.POST)
            if form.is_valid():
                nombre_usuario = form.cleaned_data.get("username")
                contraseña = form.cleaned_data.get("password")
                usuario= authenticate(username=nombre_usuario,password=contraseña)
                if usuario is not None:
                    login(request,usuario)
                    return redirect("Home") 
                else:
                    messages.error(request,"Usuario no valido")
            else:
                messages.error(request,"Alguno de sus datos es incorrecto")

    form = AuthenticationForm()
    return render(request,"login.html",{"form":form})