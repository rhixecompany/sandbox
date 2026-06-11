from django import forms
from django.forms import BoundField
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.widgets import CKEditor5Widget

from api.libary.forms_helpers import MyCustomImageWidget
from api.libary.forms_helpers import MyDateInput
from api.libary.models import Artist
from api.libary.models import Author
from api.libary.models import Category
from api.libary.models import Chapter
from api.libary.models import ChapterImage
from api.libary.models import Comic
from api.libary.models import ComicImage
from api.libary.models import Comment
from api.libary.models import Genre


class CustomeBoundField(BoundField):
    def label_tag(self, contents=None, attrs=None, label_suffix=None, tag=None):
        attrs = attrs or {}
        attrs["class"] = "block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        label_suffix = " :"
        return super().label_tag(contents, attrs, label_suffix, tag)


class CategoryForm(forms.ModelForm):
    bound_field_class = CustomeBoundField

    class Meta:
        model = Category
        fields = ("name",)


class AuthorForm(forms.ModelForm):
    bound_field_class = CustomeBoundField

    class Meta:
        model = Author
        fields = ("name",)


class ArtistForm(forms.ModelForm):
    bound_field_class = CustomeBoundField

    class Meta:
        model = Artist
        fields = ("name",)


class GenreForm(forms.ModelForm):
    bound_field_class = CustomeBoundField

    class Meta:
        model = Genre
        fields = ("name",)


class ComicForm(forms.ModelForm):
    bound_field_class = CustomeBoundField
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": _("Enter Title"),
                "class": "custom_char",
            },
        ),
    )
    slug = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": _("Enter Slug"),
                "class": "custom_char",
            },
        ),
    )
    description = forms.CharField(
        widget=CKEditor5Widget(
            attrs={"class": "django_ckeditor_5 custom_textarea", "rows": "4"},
            config_name="extends",
        ),
    )
    rating = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": _("0.0"),
                "class": "custom_char",
            },
        ),
    )
    serialization = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": _("Enter Serialization"),
                "class": "custom_char",
            },
        ),
    )
    updated_at = forms.DateField(
        widget=MyDateInput(
            attrs={
                "class": "custom_char",
            },
        ),
    )

    numchapters = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": _("0.0"),
                "class": "custom_char",
            },
        ),
    )
    numimages = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": _("0.0"),
                "class": "custom_char",
            },
        ),
    )

    class Meta:
        model = Comic
        fields = (
            "title",
            "slug",
            "description",
            "rating",
            "numchapters",
            "numimages",
            "updated_at",
            "serialization",
            "status",
            "website",
            "category",
            "author",
            "artist",
            "genres",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["website"].widget.attrs.update(
            {
                "class": "custom_select",
            },
        )
        self.fields["author"].widget.attrs.update(
            {
                "class": "custom_select",
            },
        )
        self.fields["artist"].widget.attrs.update(
            {
                "class": "custom_select",
            },
        )

        self.fields["status"].widget.attrs.update(
            {
                "class": "custom_select",
            },
        )
        self.fields["category"].widget.attrs.update(
            {
                "class": "custom_select",
            },
        )
        self.fields["genres"].widget.attrs.update(
            {
                "class": "custom_select",
            },
        )

    def clean(self):
        return self.cleaned_data


class ComicImageForm(forms.ModelForm):
    bound_field_class = CustomeBoundField
    image = forms.ImageField(
        widget=MyCustomImageWidget(
            attrs={
                "class": "custom_file",
            },
        ),
    )
    link = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "placeholder": _("Enter Link"),
                "class": "custom_char",
            },
        ),
    )

    checksum = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": _("Enter Checksum"),
                "class": "custom_char",
            },
        ),
    )

    class Meta:
        model = ComicImage
        fields = ("link", "image", "status", "checksum")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["status"].widget.attrs.update(
            {
                "class": "custom_select",
            },
        )

    def clean(self):
        return self.cleaned_data


class ChapterForm(forms.ModelForm):
    bound_field_class = CustomeBoundField
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": _("Enter Name"),
                "class": "custom_char",
            },
        ),
    )
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": _("Enter Title"),
                "class": "custom_char",
            },
        ),
    )
    slug = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": _("Enter Slug"),
                "class": "custom_char",
            },
        ),
    )

    updated_at = forms.DateField(
        widget=MyDateInput(
            attrs={
                "class": "custom_char",
            },
        ),
    )

    numimages = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": _("0.0"),
                "class": "custom_char",
            },
        ),
    )

    class Meta:
        model = Chapter
        fields = (
            "name",
            "title",
            "slug",
            "website",
            "numimages",
            "updated_at",
            "comic",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["website"].widget.attrs.update(
            {
                "class": "custom_select",
            },
        )
        self.fields["comic"].widget.attrs.update(
            {
                "class": "custom_select",
            },
        )

    def clean(self):
        return self.cleaned_data


class ChapterImageForm(forms.ModelForm):
    bound_field_class = CustomeBoundField
    image = forms.ImageField(
        widget=MyCustomImageWidget(
            attrs={
                "class": "custom_char",
            },
        ),
    )
    link = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "placeholder": _("Enter Slug"),
                "class": "custom_char",
            },
        ),
    )

    checksum = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": _("Enter Checksum"),
                "class": "custom_char",
            },
        ),
    )

    class Meta:
        model = ChapterImage
        fields = ("link", "image", "status", "checksum")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["status"].widget.attrs.update(
            {
                "class": "custom_select",
            },
        )

    def clean(self):
        return self.cleaned_data


class CommentForm(forms.ModelForm):
    bound_field_class = CustomeBoundField

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = True

    class Meta:
        model = Comment
        fields = ("text",)
        widgets = {
            "text": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5 custom_textarea", "rows": "4"},
                config_name="extends",
            ),
        }

    def clean(self):
        return self.cleaned_data
