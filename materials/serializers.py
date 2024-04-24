from rest_framework import serializers

from materials.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    """
    Переводит структуру данных в битовую последовательность
    """
    class Meta:
        """
        Определяет какие поля класса Курс будут сериализованы
        """
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    """
    Переводит структуру данных в битовую последовательность
    """
    class Meta:
        """
        Определяет какие поля класса Урок будут сериализованы
        """
        model = Lesson
        fields = '__all__'
