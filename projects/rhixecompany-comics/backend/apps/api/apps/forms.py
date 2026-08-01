from api.apps.models import Chapter, ChapterImage, Comic, ComicImage, Comment
from api.users.widgets import MyCustomCKEditorWidget, MyCustomImageWidget
from django import forms
from django.utils.translation import gettext_lazy as _


class ComicForm(forms.ModelForm):
    class Meta:
        model = Comic
        fields = (
            "title",
            "slug",
            "description",
            "rating",
            "status",
            "spider",
            "serialization",
            "url",
            "updated_at",
            "type",
            "author",
            "artist",
            "genres",
        )
        widgets = {
            "updated_at": forms.DateInput(
                attrs={
                    "type": "date",
                },
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            f = str(field)
            new_data = {
                "placeholder": _(f"Enter your {f}"),
                "class": "",
            }
            self.fields[str(field)].widget.attrs.update(new_data)


class ComicImageForm(forms.ModelForm):
    class Meta:
        model = ComicImage
        fields = ("image", "url")
        widgets = {
            "image": MyCustomImageWidget(
                attrs={"aria-describedby": "image_input_help"},
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            f = str(field)
            new_data = {
                "placeholder": _(f"Enter your {f}"),
                "class": "",
            }
            self.fields[str(field)].widget.attrs.update(new_data)


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = (
            "name",
            "title",
            "slug",
            "spider",
            "url",
            "numpages",
            "updated_at",
        )
        widgets = {
            "updated_at": forms.DateInput(
                attrs={
                    "type": "date",
                },
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            f = str(field)
            new_data = {
                "placeholder": _(f"Enter your {f}"),
                "class": "",
            }
            self.fields[str(field)].widget.attrs.update(new_data)


class ChapterImageForm(forms.ModelForm):
    class Meta:
        model = ChapterImage
        fields = ("image", "url")
        widgets = {
            "image": MyCustomImageWidget(
                attrs={"aria-describedby": "image_input_help"},
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            f = str(field)
            new_data = {
                "placeholder": _(f"Enter your {f}"),
                "class": "",
            }
            self.fields[str(field)].widget.attrs.update(new_data)


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = True

    class Meta:
        model = Comment
        fields = ("text",)
        widgets = {
            "text": MyCustomCKEditorWidget(
                attrs={
                    "rows": "6",
                    "placeholder": _("Write a comment..."),
                },
            ),
        }
