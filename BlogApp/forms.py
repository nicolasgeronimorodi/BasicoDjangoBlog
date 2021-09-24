from django import forms
from django.forms import ModelForm, widgets
from BlogApp.models import Suscripto2

from django.utils.translation import gettext_lazy as _

class FormularioNewsletter(forms.Form):
    full_Name=forms.CharField(label="Nombre y apellido", max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    email=forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'input'}))
    #########

                    

                    
        
class FormularioNewsletterModelForm(forms.ModelForm):
    nombre=forms.CharField(label='Nombre completo', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'input is-primary'})) 
    email=forms.EmailField(label='Correo', max_length=30, required=True, widget=forms.EmailInput(attrs={'class': 'input is-primary'}))
    class Meta:
        model=Suscripto2
        fields={'nombre', 'email'}