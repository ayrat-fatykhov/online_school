from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """
    Определяет поля для Курса
    """
    name = models.CharField(max_length=255, verbose_name='название')
    preview = models.ImageField(upload_to='materials/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        """
        Выводит информацию об экземпляре класса Курс
        :return: строка с информацией о курсе
        """
        return f'{self.name}'

    class Meta:
        """
        Определяет наименования модели в админке
        """
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """
    Определяет поля для Урока
    """
    name = models.CharField(max_length=255, verbose_name='название')
    preview = models.ImageField(upload_to='materials/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    url = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', related_name='lesson')

    def __str__(self):
        """
        Выводит информацию об экземпляре класса Урок
        :return: строка с информацией об уроке
        """
        return f'{self.name}, курс {self.course}'

    class Meta:
        """
        Определяет наименования модели в админке
        """
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
