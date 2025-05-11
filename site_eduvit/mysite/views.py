from django.shortcuts import render
from .models import BlogPost, Comment

def index(request):
    blogs = BlogPost.objects.all()
    title = "Главная страница"
    return render(request, template_name='mysite/blog_list.html', context={"blogs": blogs, "title": title})

def detail(request, pk):
    blog = BlogPost.objects.get(pk=pk)
    comments = Comment.objects.filter(blog=blog)
    title = blog.title

    first = blogs.first().id
    last = blogs.last()id
    count = str(request.GET.get("post"))

    return render(
        request,
        template_name='mysite/blog_detail.html',
        context={"blog": blog, "comments": comments, "title": title}
    )