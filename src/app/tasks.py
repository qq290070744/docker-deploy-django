from __future__ import absolute_import, unicode_literals
from src.celery import app
from django.core.mail import send_mail


@app.task
def send_email(title, body, email_host_user, mails):
    try:
        send_mail(title, body, email_host_user, mails)
    except Exception as e:
        print(e)
