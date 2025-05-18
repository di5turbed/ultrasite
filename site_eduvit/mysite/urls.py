from django.urls import path
from . import views

app_name = 'mysite'
urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:pk>/", views.detail, name="blog_detail"),
    path("create/", views.create_blog, name="create_blog"),
    path("profile/", views.profile, name="profile"),
    path("contacts/", views.contacts, name="contacts"),
]
