from django.db import models
from django.conf import settings
from accounts.models import User


def image_upload_path(instance, filename):
    return f'{instance.pk}/{filename}'

class ComPost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, blank=False)
    #nickname = models.CharField(max_length=12)
    content = models.TextField(max_length=3000, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    media = models.FileField(upload_to='compost_media/', blank=True, null=True)
    #writer = models.ForeignKey(User, on_delete=models.CASCADE)

class ComComment(models.Model):
    id = models.AutoField(primary_key=True)
    compost= models.ForeignKey(ComPost, blank=True, null=True, on_delete=models.CASCADE, related_name='comcomments')
    #writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=500, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.PositiveIntegerField(default=0)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

class CommunityReaction(models.Model):
    REACTION_CHOICES = (("like", "Like"), ("heart", "Heart"))
    reaction = models.CharField(choices=REACTION_CHOICES, max_length=10)
    compost = models.ForeignKey(ComPost, on_delete=models.CASCADE, related_name="reactions")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class ComReply(models.Model):
    id = models.AutoField(primary_key=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    comcomment = models.ForeignKey(ComComment, blank=False, null=False, on_delete=models.CASCADE, related_name='comreplies')
