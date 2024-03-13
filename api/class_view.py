from main .models import Post
from .serializers import *
from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,CreateAPIView
from rest_framework.response import Response
from rest_framework import status


# class List(ListAPIView):
#     queryset=Post.objects.all()
#     serializer_class=PostSerilaizer
    


# class Detail(RetrieveAPIView):
#     queryset=Post.objects.all()
#     serializer_class=PostSerilaizer



# class Create(CreateAPIView):
#     serializer_class=PostSerilaizer
#     def perform_create(self, serializer):
#         return serializer.save(author=self.request.user)
    



# class Update(UpdateAPIView):
#     serializer_class=PostSerilaizer
#     def get_queryset(self):
#         return Post.objects.filter(author=self.request.user)
    

# class Delete(DestroyAPIView):
#     def get_queryset(self):
#         return Post.objects.filter(author=self.request.user)
    


