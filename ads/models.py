from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings 

class Ad(models.Model):
    PROPERTY_TYPES = [
        ('apartment', 'Квартира'),
        ('house', 'Дом'),
        ('land', 'Земельный участок'),
        ('commercial', 'Коммерческая недвижимость'),
    ]
    STATUS_CHOICES = [
        ('active', 'Активное'),
        ('inactive', 'Неактивное'),
    ]
    SALE_RENT_CHOICES = [
        ('sale', 'Продажа'),
        ('rent', 'Аренда'),
    ]
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    sale_or_rent = models.CharField(max_length=4, choices=SALE_RENT_CHOICES)
    image = CloudinaryField('Изображение', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="Автор")
    location = models.CharField(max_length=255, verbose_name="Местоположение", blank=True, null=True)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    area = models.DecimalField(max_digits=10, decimal_places=2)
    rooms = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    

    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/accounts/{self.id}'
    

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-created_at']
