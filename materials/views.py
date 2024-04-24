from rest_framework import viewsets, generics

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    Группирует логику обработки запросов для определенного ресурса в одном классе
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonCreateView(generics.CreateAPIView):
    """
    Отвечает за создание сущности
    """
    serializer_class = LessonSerializer


class LessonListView(generics.ListAPIView):
    """
    Отвечает за отображение списка сущностей
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveView(generics.RetrieveAPIView):
    """
    Отвечает за отображение одной сущности
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateView(generics.UpdateAPIView):
    """
    Отвечает за редактирование сущности
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyView(generics.DestroyAPIView):
    """
    Отвечает за удаление сущности
    """
    queryset = Lesson.objects.all()
