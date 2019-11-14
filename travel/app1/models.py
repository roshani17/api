from django.db import models

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.
class destination(models.Model):
    name = models.CharField(max_length=30)
    disc = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='destination', on_delete=models.CASCADE)
    highlighted = models.TextField()

    


class destinationName(models.Model):
    name = models.CharField(max_length=50)