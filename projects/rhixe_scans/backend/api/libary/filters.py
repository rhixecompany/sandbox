import django_filters
from django import forms
from django.utils.translation import gettext_lazy as _

from api.libary.constants import ComicStatus
from api.libary.forms_helpers import MyMulRadioSelect
from api.libary.models import Chapter
from api.libary.models import Comic


class ComicFilterSet(django_filters.FilterSet):
    comic_title = django_filters.CharFilter(
        field_name="title",
        lookup_expr="icontains",
        widget=forms.SearchInput(  # type: ignore  # noqa: PGH003
            attrs={
                "placeholder": _("Search comics..."),
                "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500",  # noqa: E501
            },
        ),
    )
    comic_status = django_filters.MultipleChoiceFilter(
        field_name="status",
        choices=ComicStatus.choices,
        widget=MyMulRadioSelect(
            attrs={
                "multiple": "true",
            },
        ),
    )

    class Meta:
        model = Comic
        fields = ("comic_title", "comic_status")


class ChapterFilterSet(django_filters.FilterSet):
    chapter_name = django_filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
        widget=forms.SearchInput(  # type: ignore  # noqa: PGH003
            attrs={
                "placeholder": _("Search chapters..."),
                "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500",  # noqa: E501
            },
        ),
    )

    class Meta:
        model = Chapter
        fields = ("chapter_name",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields["chapter_name"].widget.attrs.update(
            {
                "placeholder": _("Search chapters..."),
            },
        )


class SearchFilterSet(django_filters.FilterSet):
    search = django_filters.CharFilter(
        field_name="title",
        lookup_expr="icontains",
        widget=forms.SearchInput(  # type: ignore  # noqa: PGH003
            attrs={
                "placeholder": _("Search"),
            },
        ),
    )
    search1 = django_filters.CharFilter(
        field_name="title",
        lookup_expr="icontains",
        widget=forms.SearchInput(  # type: ignore  # noqa: PGH003
            attrs={
                "placeholder": _("Search comics..."),
            },
        ),
    )

    class Meta:
        model = Comic
        fields = ("search", "search1")
