from django.db import models

class Reviews(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name='Имя')
    role = models.CharField(max_length=30, blank=False, verbose_name='Роль')
    text = models.TextField(blank=False, verbose_name='Текст отзыва')
    image = models.ImageField(upload_to='main_images', blank=True, null=True, verbose_name='Изображение')

    class Meta:
        db_table = 'review'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.name} | {self.role}'
    

class Order(models.Model):
    SERVICE_CHOICES = [
        ('daily-clean', 'Ежедневная уборка'),
        ('deep-clean', 'Глубокая уборка'),
        ('window-clean', 'Мытье окон'),
        ('carpet-clean', 'Химчистка ковров'),
        ('disinfection', 'Дезинфекция помещений'),
        ('furniture-car', 'Уход за мебелью'),
    ]
    
    name = models.CharField("Имя", max_length=100, blank=False)
    phone = models.CharField("Телефон", max_length=20, blank=False)
    service = models.CharField("Услуга", max_length=20, choices=SERVICE_CHOICES, blank=False)
    address = models.CharField("Адрес", max_length=255, blank=False)
    date = models.DateField("Дата", blank=False)
    time = models.TimeField("Время", blank=False)
    created_at = models.DateTimeField("Создано", auto_now_add=True)

    class Meta:
        db_table = 'order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"{self.name} - {self.service} на {self.date} в {self.time}"