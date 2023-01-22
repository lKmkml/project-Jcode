from django.db import models
from app.models import Category,CategorySub
# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=450)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='video', null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    category_sub = models.ForeignKey(CategorySub, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    price_before = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class VideoChapter(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class VideoLesson(models.Model):
    chapter = models.ForeignKey(VideoChapter, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=250)
    duration_time = models.CharField(max_length=15, null=True, blank=True)
    image = models.FileField(upload_to='video/lesson', null=True, blank=True)
    video_url = models.CharField(max_length=450, null=True, blank=True)
    is_locked = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

