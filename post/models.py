from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = {
(0, 'Draft'),
(1, 'Publish')
}

CATEGORY = {
('tech','Technology'),
('fash','Fashion'),
('others','Others')
}

class Posts(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.CharField(max_length=100,choices= CATEGORY, default='others')
    images = models.ImageField(upload_to='blog_post', default='default.jpg')


    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title
