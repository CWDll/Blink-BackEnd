from django.db import models
from accounts.models import User

# Create your models here.
class MainPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    category_choices = [
        (1, 'Category 1'), 
        (2, 'Category 2'), 
        (3, 'Category 3'), 
        (4, 'Category 4')
    ]
    category = models.CharField(default='', max_length = 10, choices=category_choices, blank=False, null=False)


    # location = 
    # category =
    # filmed_at =
    # media = models.FileField(upload_to='mainpost_media/', blank=True, null=True)

class MainPostMedia(models.Model):
    mainpost = models.ForeignKey(MainPost, on_delete=models.CASCADE, related_name='medias')
    media = models.FileField(upload_to='mainpost_media/', blank=True, null=True) #, blank=True, null=True 필요하면 집어넣기

class MainComment(models.Model):
    id = models.AutoField(primary_key=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    mainpost = models.ForeignKey(MainPost, blank=False, null=False, on_delete=models.CASCADE, related_name='comments')

class MainReply(models.Model):
    id = models.AutoField(primary_key=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    maincomment = models.ForeignKey(MainComment, blank=False, null=False, on_delete=models.CASCADE, related_name='replies')
