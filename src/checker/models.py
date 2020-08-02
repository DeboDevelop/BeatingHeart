from django.db import models

# Create your models here.
class Website(models.Model):
    """
    Class to define the model of the app:
    url - stored the url of the website
    email - stored the email where the mail will be sent if the website is down
    currently_up - boolean value to store website is up or not
    """
    url = models.URLField(unique=True)
    email = models.EmailField()
    currently_up = models.BooleanField(default=False)

    def __str__(self):
        return self.url