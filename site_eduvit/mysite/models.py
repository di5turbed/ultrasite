from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    date_published = models.DateTimeField(default=timezone.now(), verbose_name="Дата публикации")
    image = models.ImageField(upload_to="images/", verbose_name="Изображение")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", null=True, blank=True)

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse("blog:blog_detail", kwargs={"pk": self.pk})
    