from django.forms import *
from django import forms
from .models import Alumnos

class AlumnosForm(forms.ModelForm):
    class Meta: 
        model = Alumnos
        fields = ['nombre',
                  'carrera',
                  'grado',
                  'beca']
        widgets = {
            'nombre': TextInput(
                attrs={
                    'class': 'form-control'
                }
                
            ),

            'carrera': TextInput(
                attrs={
                    'class': 'form-control'
                }
                
            ),

            'grado': TextInput(
                attrs={
                    'class': 'form-control'
                }
                
            ),

            'beca': Select(
                attrs={
                    'class': 'form-select'
                }
                
            )

        }