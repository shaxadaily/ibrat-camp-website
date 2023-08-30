from django.db import models
from django.urls import reverse
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)
    image1 = models.ImageField(blank=True, null=True)
    image2 = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField()

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.pk})
