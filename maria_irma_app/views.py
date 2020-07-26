from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import cabana, plano
from django.core.mail import send_mail
from maria_irma_app.forms import formulario_ejemplo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def home(request):
    return render(request, "proyecto_web_app/home.html")


def servicios(request):
    return render(request, "proyecto_web_app/servicios.html")


def contacto(request):

    if request.method == "POST":
        formulario = formulario_ejemplo(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data

            mensaje_adjunto = info['mensaje'] + " " + info['mail']

            send_mail(info['asunto'], mensaje_adjunto, info.get('mail', 'pinares133@gmail.com'), ['pinares133@gmail.com'])

            messages.success(request, "Correo enviado con exito")
            return redirect('contacto')
        
    else:
            formulario = formulario_ejemplo()

    return render(request, "proyecto_web_app/formulario.html", {"form":formulario})    
    

#CLASES

def CabanaListView(request):
    cabana_list = cabana.objects.all().order_by('-fecha')
    page = request.GET.get('page', 1)

    paginator = Paginator(cabana_list, 6)
    try:
        cabanas = paginator.page(page)
    except PageNotAnInteger:
        cabanas = paginator.page(1)
    except EmptyPage:
        cabanas = paginator.page(paginator.num_pages)

    return render(request, 'cabanas.html', { 'cabanas': cabanas })


class CabanaDetailView(DetailView):
    model = cabana
    template_name = 'cabanas_slug.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


def PlanoListView(request):
    plano_list = plano.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(plano_list, 6)
    try:
        planos = paginator.page(page)
    except PageNotAnInteger:
        planos = paginator.page(1)
    except EmptyPage:
        planos = paginator.page(paginator.num_pages)

    return render(request, 'planos.html', { 'planos': planos })


class PlanoDetailView(DetailView):
    model = plano
    template_name = 'planos_slug.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context



