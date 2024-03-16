from django .forms import ModelForm
from .models import Post



class PostForm(ModelForm):
    class Meta:
        model=Post
        exclude=('author',)
        # fields='__all__' 

