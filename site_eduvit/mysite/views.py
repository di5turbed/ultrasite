from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost, Comment
from .forms import BlogModelForm, CommentForm
from datetime import datetime
from django.contrib.auth.decorators import login_required

def index(request):
    blogs = BlogPost.objects.all().order_by('-date_published')[:3]  # Получаем только последние 3 блога
    title = "Главная страница"
    return render(request, template_name='mysite/blog_list.html', context={"blogs": blogs, "title": title})


def news(request):
    blogs = BlogPost.objects.all()
    
    # Поиск по названию
    search_query = request.GET.get('search', '')
    if search_query:
        blogs = blogs.filter(title__icontains=search_query)
    
    # Сортировка по дате
    sort = request.GET.get('sort', 'date_desc')
    if sort == 'date_asc':
        blogs = blogs.order_by('date_published')
    else:  # date_desc
        blogs = blogs.order_by('-date_published')
    
    title = "Новости"
    return render(request, template_name='mysite/news.html', context={
        "blogs": blogs,
        "title": title,
        "search_query": search_query,
        "sort": sort
    })

def detail(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    comments = Comment.objects.filter(blog=blog)
    title = blog.title
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.author = request.user
            comment.save()
            return redirect('mysite:blog_detail', pk=pk)
    else:
        form = CommentForm()
        
    return render(
        request,
        template_name='mysite/blog_detail.html',
        context={
            "blog": blog,
            "comments": comments,
            "title": title,
            "form": form
        }
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

@login_required
def profile(request):
    user_blogs = BlogPost.objects.filter(author=request.user)
    return render(request, 'users/profile.html', {'user_blogs': user_blogs})

def contacts(request):
    title = "Контакты"
    return render(request, 'mysite/contacts.html', {'title': title})