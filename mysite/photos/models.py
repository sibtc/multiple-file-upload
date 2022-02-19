from django.db import models

class PhotoModel(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # image = models.ImageField(upload_to='photos/')
    # class Meta:
    #     ordering = ['name']

    def __str__(self):
        return self.title