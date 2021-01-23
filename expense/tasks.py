from celery import shared_task
from django.core.mail import send_mail
from expensemanager.settings import DEFAULT_FROM_EMAIL as me
from django.contrib.auth.models import User
@shared_task
def send_email_task_on_signup(user_id):
    user = User.objects.get(pk=user_id)
    user_email = user.email
    subject = 'Expense Manager'
    content = '''Welcome {}, Thank You for Signing Up in our website. You are receiving this email because your email has been associated to a registered account in our website.
    Thank You
    '''.format(user.username)
    send_mail(subject,content,me,[user_email])
