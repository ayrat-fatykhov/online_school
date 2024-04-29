from rest_framework import serializers

from materials.models import Course, Lesson


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
