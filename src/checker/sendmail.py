from django.core.mail import send_mail
from decouple import config

def sent_mail_up(url, email):
    """
    Function to send mail if website is up.
    Args:
        url (str): The url of the website
        email (str): The email where the mail will be sent
    """
    message= "The following website is up: "+url
    #Sending mail
    send_mail(
        'Website is up',
        message,
        config('EMAIL_HOST_USER'),
        [email],
        fail_silently=False,
    )

def sent_mail_down(url, email):
    """
    Function to send mail if website is down.
    Args:
        url (str): The url of the website
        email (str): The email where the mail will be sent
    """
    message= "The following website is down: "+url
    #Sending mail
    send_mail(
        'Website is down',
        message,
        config('EMAIL_HOST_USER'),
        [email],
        fail_silently=False,
    )