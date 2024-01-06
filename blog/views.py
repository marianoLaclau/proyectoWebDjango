from django.shortcuts import render
from blog.models import Post ,Categorias

# Create your views here.



def blog(request):
    
    post = Post.objects.all()
    categ = Categorias.objects.all()

    return render(request,"blog.html",{"posteo":post,"categorias":categ})