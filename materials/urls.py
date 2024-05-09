from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet, LessonCreateView, LessonListView, LessonRetrieveView, LessonUpdateView, \
    LessonDestroyView, SubscriptionListAPIView, SubscriptionCreateAPIView, SubscriptionDestroyAPIView

app_name = MaterialsConfig.name
router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create/', LessonCreateView.as_view(), name='lesson_create'),
    path('lesson/list/', LessonListView.as_view(), name='lesson_list'),
    path('lesson/view/<int:pk>/', LessonRetrieveView.as_view(), name='lesson_view'),
    path('lesson/update/<int:pk>/', LessonUpdateView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyView.as_view(), name='lesson_delete'),
    path('subscriptions/', SubscriptionListAPIView.as_view(), name='subs_list'),
    path('subscriptions/create/', SubscriptionCreateAPIView.as_view(), name='subs_create'),
    path('subscriptions/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subs_delete'),
] + router.urls
