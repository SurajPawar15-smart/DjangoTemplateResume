from django.shortcuts import render
from .models import Resume,Post,Contact
from django.views.generic import ListView
# from .forms import ContactMe


# Create your views here.
#def home(request):
#    return HttpResponse('<h1>HOME PAGE</h1>')

def home(request):
    return render(request,'resume/home.html')

def about(request):
    resume=Resume.objects.get(pk=1)
    return render(request,'resume/about.html',{"resume":resume})    

# def blog(request):
#     context={'posts':Post.objects.all}
#     return render(request,'resume/blog.html',context)

#class base views


# def blog(request):
#     post_objects=Post.objects.all()
#     item_name=request.GET.get('item_name')
#     if item_name!='' and item_name is not None:
#         post_objects=post_objects.filter(title__icontains=item_name)
#     return render(request,'resume/blog.html',{"post_pbjects":post_objects})

class PostListView(ListView):
    model=Post
    template_name='resume/blog.html'
    context_object_name='posts'
    ordering=['-date']

def portfolio(request):
    return render(request,'resume/portfolio.html')


def contact(request):
    form=Resume.objects.get(pk=1)
    return render(request,'resume/form.html',{'form':form})



