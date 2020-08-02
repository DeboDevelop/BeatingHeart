from django.core.mail import send_mail
from decouple import config

def sent_mail_up(url, email):
    message= "The following website is up: "+url
    send_mail(
        'Website is up',
        message,
        config('EMAIL_HOST_USER'),
        [email],
        fail_silently=False,
    )

def sent_mail_down(url, email):
    message= "The following website is down: "+url
    send_mail(
        'Website is down',
        message,
        config('EMAIL_HOST_USER'),
        [email],
        fail_silently=False,
    )