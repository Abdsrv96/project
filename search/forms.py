from django import forms
from ads.models import Ad

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

class AdFilterForm(forms.Form):
    q = forms.CharField(required=False, label='Поиск по названию', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}))
    min_price = forms.DecimalField(required=False, label='Минимальная цена', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Минимальная цена'}))
    max_price = forms.DecimalField(required=False, label='Максимальная цена', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Максимальная цена'}))
    location = forms.ChoiceField(choices=LOCATIONS_CHOICES, required=False, label='Местоположение', widget=forms.Select(attrs={'class': 'form-control'}))
    ordering = forms.ChoiceField(required=False, label='Сортировка', choices=[
        ('-created_at', 'Сначала новые'),
        ('created_at', 'Сначала старые'),
        ('price', 'Сначала дешёвые'),
        ('-price', 'Сначала дорогие'),
    ], widget=forms.Select(attrs={'class': 'form-control'}))
    property_type = forms.ChoiceField(
        choices=[('', 'Тип недвижимости')] + Ad.PROPERTY_TYPES,
        required=False,
        label='Тип недвижимости',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
