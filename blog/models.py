# blog/models.py
from django.db import models
from PIL import Image
from ckeditor.fields import RichTextField
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    file = models.FileField(upload_to='files/', null=True, blank=True)
    is_paid_content = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)  # 公開/非公開
    is_scheduled = models.BooleanField(default=False)  # 予約投稿
    scheduled_time = models.DateTimeField(null=True, blank=True)  # 予約投稿の日時
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 480 or img.width > 710:
                output_size = (710, 480)
                img.thumbnail(output_size)
                img.save(self.image.path)

    def __str__(self):
        return self.title

    @property
    def is_visible(self):
        now = timezone.now()
        if self.is_published:
            if self.is_scheduled:
                return self.scheduled_time and now >= self.scheduled_time
            return True
        return False
