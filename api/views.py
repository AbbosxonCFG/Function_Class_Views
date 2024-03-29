from django.shortcuts import render
from .serializers import SignUpSerailizer
from rest_framework import generics,status
from rest_framework.response import Response

from rest_framework.decorators import api_view,permission_classes,authentication_classes
from main.models import Post
from .serializers import *
from rest_framework .authentication import TokenAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

from .permissions import IsAdmin


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
@authentication_classes([])

def list_pk(request):
    username=request.GET.get('username')
    pk=request.GET.get('id')

    if username is not None:
        post=Post.objects.filter(author__username=username)
        if post.exists():
            serializer=PostSerilaizer(post,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else:
            return Response('Sahifa mavjud emas',status=404)
        
    if pk is not None:
        post=Post.objects.filter(id=pk)
        if post.exists():
            serializer=PostSerilaizer(post)
            return Response(serializer.data,status=200)
        else:
            return Response('Bu id da post mavjud emas',status=404)
        
    post=Post.objects.all().order_by('-id')
    serializer=PostSerilaizer(post,many=True)
    return Response(data=serializer.data,status=200)
    



    



@api_view(['POST'])
@authentication_classes([BasicAuthentication])
def create(request):
    if request.method == "POST":
            title = request.data.get('title')
            desc = request.data.get('desc')
            
            # Foydalanuvchi avtorizatsiyadan o'tgan bo'lishini tekshirish
            if request.user.is_authenticated:
                user = request.user
                if title and desc is not  None:
                    post = Post.objects.create(
                        author=user,
                        title=title, 
                        desc=desc,
                    )
                    serializer=PostSerilaizer(post).data
                    return Response({'message': 'Post muvafaqiyatlik yaratildi','data':serializer}, status=201)
                else:
                    return Response({"message":'malumot kiritilish kerak bolgan qatorlarni toliq kriting'},status=400)
            else:
                return Response({'message': 'Avtorizatsiyadan o`tgan foydalanuvchi kiritilishi shart'}, status=400)
            





@api_view(['PUT','DELETE'])
@permission_classes([IsAdmin])
def put_delete(request):
    post_id=request.GET.get('id')
    if request.method=='PUT':
        title = request.data.get('title')
        desc = request.data.get('desc')

        if post_id is not None:
            post=Post.objects.filter(id=post_id,author=request.user)
            if post.exists():
                post=post[0]
                if title is not None: post.title=title
                if desc is not None: post.desc=desc
                post.save()
                return Response({'massage':'post muvafaqiyatlik yangilandi'},status=200)
            else:
                return Response({'massage':'bunday sahifa yoq,yoki siz postning authori emassiz'},status=404)
        else:
            return Response({"massage":"parametrga (id) kriting "},status=404)
            
            
    if request.method=='DELETE':
        if post_id is not None:
            post=Post.objects.filter(id=post_id,author=request.user)
            if post.exists():
                post.delete()
                return Response({"massage":"post o'chirildi"},status=200)
            else:
                return Response({'massage':'bunday sahifa yoq,yoki siz postning authori emassiz'},status=404)
        else:
            return Response({"massage":"parametrga (id) kriting "},status=404)





class SignUpView(generics.GenericAPIView):
    serializer_class=SignUpSerailizer

    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            contex={
                'massage':'User created succesfully',
                'data':serializer.data

            }

            return Response(data=contex,status=201)
        return Response(data=serializer.errors,status=400)


