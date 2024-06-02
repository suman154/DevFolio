from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
    


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date_posted = models.DateField()
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    comments_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title