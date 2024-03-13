from django.db import models
from api.models import User

class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    desc=models.TextField()

    def __str__(self):
        return self.title
    
    
