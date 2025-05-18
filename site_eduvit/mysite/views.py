from django.shortcuts import render, redirect
from .models import BlogPost, Comment
from .forms import BlogModelForm
from datetime import datetime

def index(request):
    blogs = BlogPost.objects.all()
    title = "Главная страница"
    return render(request, template_name='mysite/blog_list.html', context={"blogs": blogs, "title": title})

def detail(request, pk):
    blog = BlogPost.objects.get(pk=pk)
    comments = Comment.objects.filter(blog=blog)
    title = blog.title
    return render(
        request,
        template_name='mysite/blog_detail.html',
        context={"blog": blog, "comments": comments, "title": title}
    )

def create_blog(request):
    title = "Создание блога"
    if request.method == "POST":
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user
            new_blog.date_published = datetime.now()
            new_blog.save()
    else:
        form = BlogModelForm()
    return render(request, template_name='mysite/create_update_blog.html', context= {"title": title, "form": form})