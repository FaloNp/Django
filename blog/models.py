from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    CATEGORY_LIST = [
        ('ITEM1', 'Tech & IT'),
        ('ITEM2', 'Hobbies & Fun'),
        ('ITEM3', 'Sports & Rec'),
        ('ITEM4', 'Cooking & Food'),
        ('ITEM5', 'Art & Culture'),
    ]
    CATEGORY_DEFAULT = 'ITEM1'
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, default=CATEGORY_DEFAULT, choices=CATEGORY_LIST)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"