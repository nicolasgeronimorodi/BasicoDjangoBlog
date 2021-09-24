from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('formulario', views.formulario_newsletter, name="formulario"),
    path('homepage', views.Homepage.as_view(), name="homepage")



]