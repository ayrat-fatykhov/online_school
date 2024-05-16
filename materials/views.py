from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson, CourseSubscription
from materials.paginators import CoursePaginator, LessonPaginator
from materials.serializers import CourseSerializer, LessonSerializer, SubscribeSerializer
from materials.tasks import send_course_update
from users.permissons import IsModer, IsCreator, IsUser


class CourseViewSet(viewsets.ModelViewSet):
    """
    Группирует логику обработки запросов для определенного ресурса в одном классе
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator

    def perform_create(self, serializer):
        course = serializer.save()
        course.creator = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated, ~IsModer]
        elif self.action in ['list', 'retrieve', 'update', 'partial_update']:
            permission_classes = [IsModer | IsCreator]
        elif self.action == 'destroy':
            permission_classes = [IsCreator]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def perform_update(self, serializer):
        course_id = serializer.save(creator=self.request.user).id
        send_course_update.delay(course_id)


class LessonCreateView(generics.CreateAPIView):
    """
    Отвечает за создание сущности
    """
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModer]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.creator = self.request.user
        lesson.save()


class LessonListView(generics.ListAPIView):
    """
    Отвечает за отображение списка сущностей
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = LessonPaginator


class LessonRetrieveView(generics.RetrieveAPIView):
    """
    Отвечает за отображение одной сущности
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonUpdateView(generics.UpdateAPIView):
    """
    Отвечает за редактирование сущности
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModer | IsCreator]


class LessonDestroyView(generics.DestroyAPIView):
    """
    Отвечает за удаление сущности
    """
    queryset = Lesson.objects.all()
    permission_classes = [IsCreator]


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscribeSerializer
    permission_classes = [IsAuthenticated, IsModer | IsUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SubscriptionListAPIView(generics.ListAPIView):
    serializer_class = SubscribeSerializer

    def get_queryset(self):
        return CourseSubscription.objects.filter(user=self.request.user)


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SubscribeSerializer
    queryset = CourseSubscription.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsUser]
