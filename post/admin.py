from django.contrib import admin
from post.models import Posts, Category, Comment
# Register your models here.

admin.site.register(Posts)
admin.site.register(Category)
admin.site.register(Comment)
