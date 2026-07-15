from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'producer', 'description', 'release_date', 'rating', 'poster', 'trailer_url', 'actors']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'producer': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'release_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'poster': forms.FileInput(attrs={'class': 'form-control'}),
            'trailer_url': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Наприклад: https://youtu.be/dQw4w9WgXcQ?si=C3fTQAcbI2R8AjmD'}),
            'actors': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Введіть акторів через кому (наприклад: Кіану Рівз, Керрі-Енн Мосс)'
            }),
        }