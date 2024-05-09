from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from materials.models import Course, Lesson, CourseSubscription
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        self.user = User.objects.create(id=1, email='test@test.com', password='123123')
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(name='test_course', description='test_desc')
        self.lesson = Lesson.objects.create(name='test_lesson', description='test_desc',
                                            url='https://youtube.com/',
                                            course=self.course, creator=self.user)

    def test_create_lesson(self):
        data = {'name': 'test', 'description': 'test',
                'course': self.course.id, 'url': 'https://youtube.com/',
                'creator': self.user.id}
        url = reverse('materials:lesson_create')
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Lesson.objects.filter(name=data['name']).exists())

    def test_retrieve_lesson(self):
        url = reverse('materials:lesson_view', kwargs={'pk': self.lesson.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.lesson.name)

    def test_update_lesson(self):
        url = reverse('materials:lesson_update', kwargs={'pk': self.lesson.pk})
        data = {'name': 'Updating_test', 'description': 'Updating_test'}
        response = self.client.patch(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.name, data['name'])

    def test_lesson_delete(self):
        response = self.client.delete(
            reverse('materials:lesson_delete', args=[self.lesson.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Lesson.objects.count(),
            0
        )


class SubscriptionAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@sky.pro', is_active=True)
        self.user.set_password('test_password')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(name='Test course')
        self.lesson = Lesson.objects.create(
            name='Test lesson',
            description='Test description',
            course=self.course,
            creator=self.user,
        )
        self.subscription = CourseSubscription.objects.create(
            user=self.user,
            course=self.course,
        )

    def test_subscription_create(self):
        course = Course.objects.create(name='Test course 2')
        course.save()

        data = {
            'course': course.id,
            'user': self.user.id
        }
        response = self.client.post(
            reverse('materials:subs_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            CourseSubscription.objects.count(),
            2
        )

    def test_subscription_list(self):
        response = self.client.get(
            reverse('materials:subs_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{'id': self.subscription.id, 'is_subscribed': False, 'course': self.subscription.course.id,
              'user': self.subscription.user.id}]
        )

    def test_subscription_delete(self):
        response = self.client.delete(
            reverse('materials:subs_delete', args=[self.subscription.id])
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            CourseSubscription.objects.count(),
            0
        )
