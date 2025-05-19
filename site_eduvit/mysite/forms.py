from django import forms
from mysite.models import BlogPost, Comment
from django.forms import ModelForm


class BlogModelForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "content", "image"]

    def __init__(self, *args, **kwargs):
        super(BlogModelForm, self).__init__(*args, **kwargs)
        
        # Настройка поля заголовка
        self.fields["title"].label = ""
        self.fields["title"].widget = forms.TextInput(
            attrs={
                "placeholder": "Заголовок блога",
                "class": "form-control",
            }
        )

        # Настройка поля содержания
        self.fields["content"].label = ""
        self.fields["content"].widget = forms.Textarea(
            attrs={
                "placeholder": "Содержание блога",
                "class": "form-control",
                "rows": 10,
            }
        )

        # Настройка поля изображения
        self.fields["image"].label = ""
        self.fields["image"].widget = forms.FileInput(
            attrs={
                "class": "form-control",
                "accept": "image/*",
            }
        )

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        
        # Настройка поля текста комментария
        self.fields["text"].label = ""
        self.fields["text"].widget = forms.Textarea(
            attrs={
                "placeholder": "Напишите ваш комментарий...",
                "class": "form-control",
                "rows": 3,
            }
        )