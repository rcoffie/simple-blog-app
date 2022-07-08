from django.forms import ModelForm
from post.models import Posts

class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['title','author','content','status','category', 'images']
