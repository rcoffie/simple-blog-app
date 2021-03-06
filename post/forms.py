from django.forms import ModelForm

from post.models import Comment, Posts


class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ["title", "content", "status", "category", "images"]


class ReplyForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["comments"]
