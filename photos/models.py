from django.db import models
import os


class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


# Upload NFT Collection Folder Form
def upload_function(instance, filename):
    get_base_dir = instance.base_dir
    path = os.path.join(str(get_base_dir))
    return path

class Feed(models.Model):
    directories = models.TextField(blank=False, max_length=10000)


class FeedFile(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)

    base_dir = models.CharField(max_length=100)
    file = models.FileField(upload_to=upload_function)
