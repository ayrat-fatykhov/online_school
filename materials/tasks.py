from datetime import timezone, datetime

import pytz
from celery import shared_task
from django.core.mail import send_mail

from config import settings
from materials.models import CourseSubscription
from users.models import User


@shared_task
def send_course_update(course_id):
    for sub in CourseSubscription.objects.filter(course_id=course_id):
        send_mail(
            subject='Обновление курса',
            message=f'Курс {sub.course} был обновлен',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[sub.user.email]
        )


@shared_task
def check_last_login():
    users = User.objects.filter(is_active=True)
    if users.exists():
        for user in users:
            if datetime.datetime.now(pytz.timezone("UTC")) - user.last_login > datetime.timedelta(weeks=4):
                user.is_active = False
                user.save()
