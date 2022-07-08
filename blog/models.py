from django.db import models
from django.conf import settings


class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.title
