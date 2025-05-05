from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    date_published = models.DateTimeField(default=timezone.now(), verbose_name="Дата публикации")
    image = models.ImageField(upload_to="blog", )