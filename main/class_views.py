from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from .models import Post
from django .views.generic import ListView,CreateView,DeleteView,DetailView,UpdateView
from django .urls import reverse_lazy 
from .forms import PostForm





class List(ListView):
    model = Post
    template_name = 'list.html'
    context_object_name = 'list'
    def get_queryset(self):
        return Post.objects.all().order_by('-id')

    # def get_queryset(self):
        # try:
            # return Post.objects.filter(author=self.request.user)
        # except:
            # self.template_name = 'test.html'  
            

class Detail(DetailView):
    model=Post
    context_object_name='detail'
    template_name='detail.html'



class Create(CreateView):
    model=Post
    form_class=PostForm
    template_name='create.html'
    success_url=reverse_lazy('list')
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        return super(Create, self).form_valid(form)
    



class Update(UpdateView):
    model=Post
    form_class=PostForm
    template_name='create.html'
    success_url=reverse_lazy('list')
    
    def get_queryset(self):
        try:
            return Post.objects.filter(author=self.request.user)
        except:
            self.template_name = 'test.html'


# class Delete(DeleteView):
#     model=Post
#     template_name='delete.html'
#     success_url=reverse_lazy('list')

#     def get_queryset(self):
#         return Post.objects.filter(author=self.request.user)
    


def delete(request,pk):
    author=request.user
    post=Post.objects.get(id=pk,author=author)   
    post.delete()   
    return redirect('list')
        
    

def test(request):
    # return HttpResponse('salom')
    return render(request,'test.html')
       





  
