# forms.py

from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control bg-light border-0',
                'placeholder': 'Ваше имя',
                'style': 'height: 55px;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control bg-light border-0',
                'placeholder': 'Ваш email',
                'style': 'height: 55px;'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control bg-light border-0',
                'placeholder': 'Сообщение',
                'rows': 5
            }),
        }

