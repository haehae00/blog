from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator, MaxValueValidator

class Posting(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # grade = models.IntegerField(default=0)
    body = RichTextUploadingField()

    def __str__(self):
        return self.title


# class Photo(models.Model):
#     post = models.ForeignKey(Posting, on_delete=models.CASCADE, null=True)
#     image = models.ImageField(upload_to='images/', blank=True, null=True)