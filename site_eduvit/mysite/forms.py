from django import forms
from mysite.models import BlogPost
from django.forms import ModelForm


class BlogModelForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "content", "image"]

    def __init__(self, *args, **kwargs):
        super(BlogModelForm, self).__init__(*args, **kwargs)
        self.fields["title"].help_text = ""
        self.fields["title"].label = ""
        self.fields["title"].widget = forms.Textarea(
            attrs={
                "placeholder": "Название блога",
                "rows": 1,
                "class": "form-control",
            }
        )

        self.fields["title"].help_text = ""
        self.fields["title"].label = ""
        self.fields["title"].widget = forms.Textarea(
            attrs={
                "placeholder": "Название",
                "rows": 10,
                "class": "form-control",
            }
        )