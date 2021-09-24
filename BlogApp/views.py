from django.http.response import HttpResponse
from BlogApp.forms import FormularioNewsletterModelForm
from django.shortcuts import render, redirect
from .models import Post
from django.views import generic


# Create your views here.
def index(request):
    return render(request, 'BlogApp/index.html')

def about(request):
    return render(request, 'BlogApp/sobrenosotros.html')

def formulario_newsletter(request):
    if request.method=="POST":
        form=FormularioNewsletterModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(f"Los datos ingresados son validos")
        else:
            return HttpResponse(f"Los datos ingresados no son validos")
    form=FormularioNewsletterModelForm()
    ctx={"formulario": form}
    return render(request, 'BlogApp/formulario.html', ctx)



###########
class Homepage(generic.ListView):
    queryset=Post.objects.filter(status=1).order_by('-creado_el')
    context_object_name='post_list'
    template_name='BlogApp/homepage.html'