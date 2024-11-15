from django import forms
from .models import *

class CECS_CandidatesForm(forms.ModelForm):
   class Meta:
      model = CECS_Candidate
      exclude = ('voters',)
      fields = ('fullname', 'photo', 'bio', 'position')
      position_choices = (
         ('President','President'),
         ('Vice_President','Vice_President'),
         ('Treasurer','Treasurer'),
         ('Secretary','Secretary'),
         ('Event_Coordinator','Event_Coordinator'),
         ('Sports_and_Recreation_Officer','Sports_and_Recreation_Officer'),
         ('Cultural_affairs_officer','Cultural_affairs_officer'),
         ('Department_Representative','Department_Representative'),
      )
      widgets = {
         'photo': forms.FileInput(attrs={'type': 'file'}),
         'fullname':forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder':'Full name' }),
         'bio':forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Tell us about yourself and your motto' }),
         'position':forms.Select(choices=position_choices,attrs={'class': 'form-control', 'placeholder':'Position' }),
      }

class CSM_CandidatesForm(forms.ModelForm):
   class Meta:
      model = CSM_Candidate
      exclude = ('voters',)
      fields = ('fullname', 'photo', 'bio', 'position')
      position_choices = (
         ('President','President'),
         ('Vice_President','Vice_President'),
         ('Treasurer','Treasurer'),
         ('Secretary','Secretary'),
         ('Event_Coordinator','Event_Coordinator'),
         ('Sports_and_Recreation_Officer','Sports_and_Recreation_Officer'),
         ('Cultural_affairs_officer','Cultural_affairs_officer'),
         ('Department_Representative','Department_Representative'),
      )
      widgets = {
         'photo': forms.FileInput(attrs={'type': 'file'}),
         'fullname':forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder':'Full name' }),
         'bio':forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Tell us about yourself and your motto' }),
         'position':forms.Select(choices=position_choices,attrs={'class': 'form-control', 'placeholder':'Position' }),
      }
