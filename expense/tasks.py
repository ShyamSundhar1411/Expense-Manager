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
Best Regards,
Code Busters
    '''.format(user.username)
    send_mail(subject,content,me,[user_email])
@shared_task
def send_email_alert(user_id):
    user = User.objects.get(pk=user_id)
    user_email = user.email
    subject = 'Expense Manager'
    content = '''Hi {}, Hope you are doing well. We have noticed that your total expenses are higher than the allocated budgets. This is a kind Reminder, So that you can manage your expenses accordingly in these categories [food/automobile/water supply/electricity/entertainment/others].
Thank You
Best Regards,
Code Busters
    '''.format(user.username)
    send_mail(subject,content,me,[user_email])
@shared_task
def send_email_alert_funds(user_id):
    user = User.objects.get(pk=user_id)
    user_email = user.email
    subject = 'Expense Manager'
    content = '''Hi {}, Hope you are doing well. We have noticed that your total expenses has exceeded than the allocated budgets.Your account is not having sufficient funds.So We Remind you that Your initial expense value will be deducted from the new Budget amount. Your Account is locked until then'
Thank You
Best Regards,
Code Busters
    '''.format(user.username)
    send_mail(subject,content,me,[user_email])
