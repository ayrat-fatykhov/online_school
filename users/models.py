from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Определяет поля для модели 'Пользватель
    '"""
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)

    #Реализуют возможность взаимодействия с пользователем через email
    #(по умолчанию установлено поле 'имя пользователя')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    date = models.DateTimeField(auto_now=True, verbose_name='дата')
    payed_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс')
    payed_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок')
    sum = models.PositiveIntegerField(verbose_name='сумма оплаты')
    pay_approach = models.CharField(max_length=100, verbose_name='способ оплаты')
    session_id = models.CharField(max_length=255, verbose_name='id сессии', **NULLABLE)
    link = models.URLField(max_length=400, verbose_name='ссылка на оплату', **NULLABLE)

    def __str__(self):
        return f'{self.payed_course} {self.payed_lesson}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
