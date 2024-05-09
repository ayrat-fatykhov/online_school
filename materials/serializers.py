from rest_framework import serializers

from materials.models import Course, Lesson, CourseSubscription
from materials.validators import UrlValidator


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
        validators = [UrlValidator(url='url')]


class CourseSerializer(serializers.ModelSerializer):
    """
    Переводит структуру данных в битовую последовательность
    """
    lesson_amount = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)

    class Meta:
        """
        Определяет какие поля класса Курс будут сериализованы
        """
        model = Course
        fields = '__all__'

    def get_lesson_amount(self, instance):
        return Lesson.objects.filter(course=instance).count()


class SubscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseSubscription
        fields = '__all__'
        extra_kwargs = {'is_subscribed': {'default': True}}
