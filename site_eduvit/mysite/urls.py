from django.urls import path
from . import views

app_name = 'mysite'
urlpatterns = [
    path("", views.index, name="index"),
    path("blog/<int:pk>/", views.detail, name="blog_detail"),
]
