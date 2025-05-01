from django import forms
from .models import Ad

LOCATIONS_CHOICES = [
    ('', 'Выберите местоположение'),
    ('Almaty', 'Алматы'),
    ('Astana', 'Астана'),
    ('Shymkent', 'Шымкент'),
    ('Karaganda', 'Караганда'),
    ('Aktobe', 'Актау'),
    ('Semey', 'Семей'),
    ('Kostanay', 'Костанай'),
    ('Pavlodar', 'Павлодар'),
    ('Taraz', 'Тараз'),
]
class AdForm(forms.ModelForm):
    location = forms.ChoiceField(
        choices=LOCATIONS_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    property_type = forms.ChoiceField(
        choices=Ad.PROPERTY_TYPES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    sale_or_rent = forms.ChoiceField(
        choices=Ad.SALE_RENT_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    status = forms.ChoiceField(
        choices=Ad.STATUS_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'property_type', 'image', 'location', 'sale_or_rent', 'area', 'rooms', 'address', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите цену'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите площадь'}),
            'rooms': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите кол-во комнат'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите адресс'}),
        }