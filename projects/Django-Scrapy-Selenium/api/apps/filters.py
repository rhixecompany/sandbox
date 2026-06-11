import django_filters
from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from api.apps.models import Chapter
from api.apps.models import Comic
from api.apps.models import ComicStatus
from api.apps.models import Genre
from api.apps.models import Type
from api.users.models import User
from api.users.widgets import MyCheckboxSelectMultiple
from api.users.widgets import MyRadioSelect


class Order(models.TextChoices):
    LAST_UPDATES = "-updated_at", "Last Updated"
    RATING = "-rating", "Rating"
    NAMEZ = "-title", "Name (Z-A)"
    NAMEA = "title", "Name (A-Z)"


class ChapterFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )

    class Meta:
        model = Chapter
        fields = ("name",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields["name"].widget.attrs.update(
            {
                "placeholder": _("Search for chapters"),
                "class": "",
                "hx-get": reverse_lazy("chapters:chapter_list"),
                "hx-trigger": "keyup[target.value.length    >   3]    changed delay:1s",
                "hx-target": "#container",
                "hx-indicator": ".progress",
                "hx-swap": "outerHTML",
                "script": "on htmx:afterOnLoad set my value to ''",
            },
        )


class MyMultipleChoiceFilter(django_filters.ModelMultipleChoiceFilter):
    def filter(self, qs, value):
        if value:
            qs = super().filter(qs, value)
        return qs


class ComicFilter(django_filters.FilterSet):
    type = MyMultipleChoiceFilter(
        queryset=Type.objects.all(),
        widget=MyCheckboxSelectMultiple,
        field_name="type__name",
        lookup_expr="in",
        to_field_name="name",
    )
    genres = MyMultipleChoiceFilter(
        queryset=Genre.objects.all(),
        widget=MyCheckboxSelectMultiple,
        lookup_expr="in",
        field_name="genres__name",
        to_field_name="name",
    )
    status = django_filters.ChoiceFilter(
        choices=ComicStatus.choices,
        empty_label=None,
        widget=MyRadioSelect(),
    )
    updated_at = django_filters.ChoiceFilter(
        choices=Order.choices,
        empty_label=None,
        widget=MyRadioSelect(),
    )

    title = django_filters.CharFilter(
        field_name="title",
        lookup_expr="icontains",
    )

    class Meta:
        model = Comic
        fields = ("title", "type", "status", "genres", "updated_at")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields["title"].widget.attrs.update(
            {
                "placeholder": _("Search for comics"),
                "class": "",
                "type": "search",
                "hx-get": reverse_lazy("comics:comic_list"),
                "hx-trigger": "keyup[target.value.length    >   3]    changed delay:1s",
                "hx-target": "#container",
                "hx-indicator": ".progress",
                "hx-swap": "outerHTML",
                "script": "on htmx:afterOnLoad set my value to ''",
                "_": "on input show <tbody>tr/> in closest <table/> when its textContent.toLowerCase() contains my value.toLowerCase()",  # noqa: E501
            },
        )
        self.form.fields["genres"].widget.attrs.update(
            {
                "class": "",
            },
        )
        self.form.fields["type"].widget.attrs.update(
            {
                "class": "",
            },
        )


class UserFilter(django_filters.FilterSet):
    email = django_filters.CharFilter(
        field_name="email",
        lookup_expr="icontains",
    )

    class Meta:
        model = User
        fields = ("email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields["email"].widget.attrs.update(
            {
                "placeholder": _("Search for users"),
                "class": "",
                "hx-get": reverse_lazy("users:user_list"),
                "hx-trigger": "keyup[target.value.length    >   3]    changed delay:1s",
                "hx-target": "#container",
                "hx-indicator": ".progress",
                "hx-swap": "outerHTML",
                "script": "on htmx:afterOnLoad set my value to ''",
            },
        )


class SearchFilter(django_filters.FilterSet):
    type = MyMultipleChoiceFilter(
        queryset=Type.objects.all(),
        widget=MyCheckboxSelectMultiple,
        field_name="type__name",
        lookup_expr="in",
        to_field_name="name",
    )
    genres = MyMultipleChoiceFilter(
        queryset=Genre.objects.all(),
        widget=MyCheckboxSelectMultiple,
        lookup_expr="in",
        field_name="genres__name",
        to_field_name="name",
    )
    status = django_filters.ChoiceFilter(
        choices=ComicStatus.choices,
        empty_label=None,
        widget=MyRadioSelect(),
    )
    updated_at = django_filters.ChoiceFilter(
        choices=Order.choices,
        empty_label=None,
        widget=MyRadioSelect(),
    )

    search = django_filters.CharFilter(
        field_name="title",
        lookup_expr="icontains",
    )

    class Meta:
        model = Comic
        fields = ("search", "type", "status", "genres", "updated_at")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields["search"].widget.attrs.update(
            {
                "placeholder": _("Search for comics"),
                "class": "",
            },
        )
        self.form.fields["genres"].widget.attrs.update(
            {
                "class": "",
            },
        )
        self.form.fields["type"].widget.attrs.update(
            {
                "class": "",
            },
        )
