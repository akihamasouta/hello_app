# -*- coding: utf-8 -*-
from django import forms
from . models import Player_Name, Jobs, Postion


class Add_Player_Form(forms.ModelForm):
    class Meta:
        model = Player_Name
        fields = ['name']
        
    
class Job_Name_Form(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['job']
        
class Postion_Form(forms.ModelForm):
    class Meta:
        model = Postion
        fields = ['wolf', 'citizen', 'hunter', 'diviner', 'traitor', 'psychic']