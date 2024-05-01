from celery import shared_task
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail


@shared_task(name='Send mail')
def task_register_email(user_id):
    user = User.objects.get(user_id)

    subject = f'Welcome {user.username}!'
    message = 'This is greeting message'

    try:
        send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])
    except:
        print('send_mail() imitation\n email has been send!')