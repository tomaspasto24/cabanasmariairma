from django import forms
from maria_irma_app import views

class formulario_ejemplo(forms.Form):

    mail = forms.EmailField(widget=forms.EmailInput(attrs={
        'type':"email", 
        'class':"center",
    }))
    asunto = forms.CharField(widget=forms.TextInput(attrs={
        'type':"text", 
        'class':"center", 
    }))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={
        'class':"center",
        'rows':"3",
    }))
    