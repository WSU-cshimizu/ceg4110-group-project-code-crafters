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



class CLA_CandidatesForm(forms.ModelForm):
   class Meta:
      model = CLA_Candidate
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


class CBUS_CandidatesForm(forms.ModelForm):
   class Meta:
      model = CBUS_Candidate
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


class MAIN_CandidatesForm(forms.ModelForm):
   class Meta:
      model = MAIN_Candidate
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


class ScheduleForm(forms.ModelForm):
   class Meta:
      model = votingschedule
      fields = ('department', 'start', 'end')
      widgets = {
         'department':forms.Select(attrs={'class': 'form-control' }),
         'start':forms.TextInput(attrs={'type': 'date','class': 'form-control' }),
         'end':forms.TextInput(attrs={'type': 'date','class': 'form-control' }),
      }


class UpdateScheduleForm(forms.ModelForm):
   class Meta:
      model = votingschedule
      exclude = ('department',)
      fields = ('start', 'end')
      widgets = {
         'start':forms.TextInput(attrs={'type': 'date','class': 'form-control' }),
         'end':forms.TextInput(attrs={'type': 'date','class': 'form-control' }),
      }


