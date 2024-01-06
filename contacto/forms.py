from django import forms


#Clase Formulario para usar en las vistas

class Formulario(forms.Form):
    nombre = forms.CharField(label="Nombre",required=True,max_length=100)
    mail = forms.CharField(label="Email",required=True,max_length=100)
    contenido = forms.CharField(label="Contenido",widget=(forms.Textarea),required=True,max_length=200)
    
    
