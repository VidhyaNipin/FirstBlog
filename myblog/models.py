from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')

)


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


# def post_save_receiver(sender, instance, created, **kwargs):
#     pass
#
#
# post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)
