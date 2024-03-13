from django.shortcuts import render,redirect,HttpResponse
from .forms import PostForm
from .models import Post
from django .urls import reverse_lazy

from django.contrib.auth.decorators import login_required


def list(request):
    post=Post.objects.all().order_by('-id')
    contex={
        'list':post
    }
    return render(request,'list.html',contex)



def detail(request,pk):
    post=Post.objects.get(id=pk)
    contex={
        'detail':post
    }
    return render(request,'detail.html',contex)




@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Yaratilgan malumotni avtorini avtorizatsiyadan o'tgan foydalanuvchiga tenglashtiramiz
            post.save()
            return redirect('list')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'create.html', context)





def update(request,pk):
    try:
        post=Post.objects.get(id=pk,author=request.user)
        form=PostForm(instance=post)
        if request.method=='POST':
            form=PostForm(request.POST,instance=post)
            if form.is_valid():
                form.save()
                return redirect('list')
        contex={
            'form':form
        }
        return render(request,'create.html',contex)
    except:
        return render(request,'test.html')



def delete(request,pk):
    try:
        author=request.user
        post=Post.objects.get(id=pk,author=author)   
        post.delete()   
        return redirect('list')
    except:
        return render(request,'test.html')
    



from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')
