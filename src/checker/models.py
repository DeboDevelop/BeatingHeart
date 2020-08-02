from django.db import models

# Create your models here.
class Website(models.Model):
    url = models.URLField(unique=True)
    email = models.EmailField()
    currently_up = models.BooleanField(default=False)

    def __str__(self):
        return self.url