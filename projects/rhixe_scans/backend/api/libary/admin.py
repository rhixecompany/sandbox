from django.contrib import admin
from django.contrib.postgres.fields import ArrayField
from django.db import models
from import_export.admin import ImportExportModelAdmin
from import_export.forms import ExportForm
from import_export.forms import ImportForm
from unfold.admin import ModelAdmin
from unfold.admin import TabularInline
from unfold.contrib.filters.admin import RangeDateFilter
from unfold.contrib.filters.admin import RangeDateTimeFilter
from unfold.contrib.forms.widgets import ArrayWidget
from unfold.contrib.forms.widgets import WysiwygWidget

from api.libary.constants import ComicStatus
from api.libary.models import Artist
from api.libary.models import Author
from api.libary.models import Category
from api.libary.models import Chapter
from api.libary.models import ChapterImage
from api.libary.models import Comic
from api.libary.models import ComicImage
from api.libary.models import Comment
from api.libary.models import Genre
from api.libary.models import UserComic
from api.libary.models import Website
from api.users.admin_helpers import CustomDropdownFilter
from api.users.admin_helpers import CustomTextFilter


class CommentInline(TabularInline):
    model = Comment
    tab = True


class ComicInline(TabularInline):
    model = Comic
    tab = True


class ComicImageInline(TabularInline):
    model = ComicImage
    tab = True


class ChapterImageInline(TabularInline):
    model = ChapterImage
    tab = True


class ChapterInline(TabularInline):
    model = Chapter
    tab = True


@admin.register(Comic)
class ComicAdminClass(ModelAdmin, ImportExportModelAdmin):
    # Display fields in changeform in compressed mode
    compressed_fields = True  # Default: False

    # Warn before leaving unsaved changes in changeform
    warn_unsaved_form = True  # Default: False

    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }
    model = Comic  # type: ignore  # noqa: PGH003
    search_fields = (
        "title",
        "slug",
    )
    # Display submit button in filters
    list_filter_submit = True

    list_filter = (
        CustomTextFilter,
        CustomDropdownFilter,
        "title",
        "slug",
        ("updated_at", RangeDateFilter),  # Date filter
        ("created_at", RangeDateTimeFilter),  # Datetime filter
    )

    list_display = ("title", "slug")
    inlines = [ChapterInline, ComicImageInline]

    # Display changelist in fullwidth
    list_fullwidth = False

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail
    actions = [
        "comic_completed_action",
        "comic_ongoing_action",
        "comic_hiatus_action",
        "comic_dropped_action",
        "comic_season_end_action",
        "comic_coming_soon_action",
    ]
    import_form_class = ImportForm
    export_form_class = ExportForm
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        ArrayField: {
            "widget": ArrayWidget,
        },
    }

    @admin.action(description="Mark selected Comic as completed")
    def comic_completed_action(self, request, queryset):
        comics_to_comp = queryset.exclude(status=ComicStatus.COMPLETED)
        comics = list(comics_to_comp)

        comics_to_comp.update(status=ComicStatus.COMPLETED)

        for comic in comics:
            user = comic.user
            user.email_user(
                "Your comic has been completed",
                f"Dear {user.username}, \n\nYour comic with Title {comic.title} has been completed.",  # noqa: E501
                f"{user.email}",
                fail_silently=False,
            )
        self.message_user(
            request,
            "Selected comics have been marked as completed and users have been notified.",  # noqa: E501
        )

    @admin.action(description="Mark selected Comic as ongoing")
    def comic_ongoing_action(self, request, queryset):
        comics_to_comp = queryset.exclude(status=ComicStatus.ONGOING)
        comics = list(comics_to_comp)

        comics_to_comp.update(status=ComicStatus.ONGOING)

        for comic in comics:
            user = comic.user
            user.email_user(
                "Your comic has been ongoing",
                f"Dear {user.username}, \n\nYour comic with Title {comic.title} has been ongoing.",  # noqa: E501
                f"{user.email}",
                fail_silently=False,
            )
        self.message_user(
            request,
            "Selected comics have been marked as ongoing and users have been notified.",
        )

    @admin.action(description="Mark selected Comic as hiatus")
    def comic_hiatus_action(self, request, queryset):
        comics_to_comp = queryset.exclude(status=ComicStatus.HIATUS)
        comics = list(comics_to_comp)

        comics_to_comp.update(status=ComicStatus.HIATUS)

        for comic in comics:
            user = comic.user
            user.email_user(
                "Your comic has been hiatus",
                f"Dear {user.username}, \n\nYour comic with Title {comic.title} has been hiatus.",  # noqa: E501
                f"{user.email}",
                fail_silently=False,
            )
        self.message_user(
            request,
            "Selected comics have been marked as hiatus and users have been notified.",
        )

    @admin.action(description="Mark selected Comic as dropped")
    def comic_dropped_action(self, request, queryset):
        comics_to_comp = queryset.exclude(status=ComicStatus.DROPPED)
        comics = list(comics_to_comp)

        comics_to_comp.update(status=ComicStatus.DROPPED)

        for comic in comics:
            user = comic.user
            user.email_user(
                "Your comic has been dropped",
                f"Dear {user.username}, \n\nYour comic with Title {comic.title} has been dropped.",  # noqa: E501
                f"{user.email}",
                fail_silently=False,
            )
        self.message_user(
            request,
            "Selected comics have been marked as dropped and users have been notified.",
        )

    @admin.action(description="Mark selected Comic as Season End")
    def comic_season_end_action(self, request, queryset):
        comics_to_comp = queryset.exclude(status=ComicStatus.SEASON_END)
        comics = list(comics_to_comp)

        comics_to_comp.update(status=ComicStatus.SEASON_END)

        for comic in comics:
            user = comic.user
            user.email_user(
                "Your comic has been season_end",
                f"Dear {user.username}, \n\nYour comic with Title {comic.title} has been Season End.",  # noqa: E501
                f"{user.email}",
                fail_silently=False,
            )
        self.message_user(
            request,
            "Selected comics have been marked as Season End and users have been notified.",  # noqa: E501
        )

    @admin.action(description="Mark selected Comic as Coming Soon")
    def comic_coming_soon_action(self, request, queryset):
        comics_to_comp = queryset.exclude(status=ComicStatus.COMING_SOON)
        comics = list(comics_to_comp)

        comics_to_comp.update(status=ComicStatus.COMING_SOON)

        for comic in comics:
            user = comic.user
            user.email_user(
                "Your comic has been coming_soon",
                f"Dear {user.username}, \n\nYour comic with Title {comic.title} has been Coming Soon.",  # noqa: E501
                f"{user.email}",
                fail_silently=False,
            )
        self.message_user(
            request,
            "Selected comics have been marked as Coming Soon and users have been notified.",  # noqa: E501
        )


@admin.register(Chapter)
class ChapterAdminClass(ModelAdmin, ImportExportModelAdmin):
    # Display fields in changeform in compressed mode
    compressed_fields = True  # Default: False

    # Warn before leaving unsaved changes in changeform
    warn_unsaved_form = True  # Default: False

    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }
    model = Chapter  # type: ignore  # noqa: PGH003
    search_fields = (
        "name",
        "comic__title",
    )
    # Display submit button in filters
    list_filter_submit = True

    list_filter = (
        CustomTextFilter,
        CustomDropdownFilter,
        "name",
        "slug",
        ("updated_at", RangeDateFilter),  # Date filter
        ("created_at", RangeDateTimeFilter),  # Datetime filter
    )

    list_display = ("name", "slug")
    inlines = [ChapterImageInline, CommentInline]

    # Display changelist in fullwidth
    list_fullwidth = False

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail
    actions = []
    import_form_class = ImportForm
    export_form_class = ExportForm
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        ArrayField: {
            "widget": ArrayWidget,
        },
    }


@admin.register(ComicImage)
class ComicImageAdminClass(ModelAdmin, ImportExportModelAdmin):
    # Display fields in changeform in compressed mode
    compressed_fields = True  # Default: False

    # Warn before leaving unsaved changes in changeform
    warn_unsaved_form = True  # Default: False

    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }
    model = ComicImage  # type: ignore  # noqa: PGH003
    search_fields = (
        "link",
        # "image",
    )
    # Display submit button in filters
    list_filter_submit = True

    list_filter = (
        CustomTextFilter,
        CustomDropdownFilter,
        "link",
        # "image",
    )

    list_display = (
        "pk",
        "link",
    )
    inlines = []

    # Display changelist in fullwidth
    list_fullwidth = False

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail
    actions = []
    import_form_class = ImportForm
    export_form_class = ExportForm
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        ArrayField: {
            "widget": ArrayWidget,
        },
    }


@admin.register(ChapterImage)
class ChapterImageAdminClass(ModelAdmin, ImportExportModelAdmin):
    # Display fields in changeform in compressed mode
    compressed_fields = True  # Default: False

    # Warn before leaving unsaved changes in changeform
    warn_unsaved_form = True  # Default: False

    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }
    model = ChapterImage  # type: ignore  # noqa: PGH003
    search_fields = (
        "link",
        # "image",
        "chapter__slug",
        "chapter__name",
        "comic__title",
    )
    # Display submit button in filters
    list_filter_submit = True

    list_filter = (
        CustomTextFilter,
        CustomDropdownFilter,
        "link",
        # "image",
    )

    list_display = (
        "pk",
        "link",
    )
    inlines = []

    # Display changelist in fullwidth
    list_fullwidth = False

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail
    actions = []
    import_form_class = ImportForm
    export_form_class = ExportForm
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        ArrayField: {
            "widget": ArrayWidget,
        },
    }


@admin.register(Genre)
class GenreAdminClass(ModelAdmin, ImportExportModelAdmin):
    # Display fields in changeform in compressed mode
    compressed_fields = True  # Default: False

    # Warn before leaving unsaved changes in changeform
    warn_unsaved_form = True  # Default: False

    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }
    model = Genre  # type: ignore  # noqa: PGH003
    search_fields = ("name",)
    # Display submit button in filters
    list_filter_submit = True

    list_filter = (
        CustomTextFilter,
        CustomDropdownFilter,
        "name",
    )

    list_display = ("name",)
    inlines = []

    # Display changelist in fullwidth
    list_fullwidth = False

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail
    actions = []
    import_form_class = ImportForm
    export_form_class = ExportForm
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        ArrayField: {
            "widget": ArrayWidget,
        },
    }


@admin.register(Category)
class CategoryAdminClass(ModelAdmin, ImportExportModelAdmin):
    # Display fields in changeform in compressed mode
    compressed_fields = True  # Default: False

    # Warn before leaving unsaved changes in changeform
    warn_unsaved_form = True  # Default: False

    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }
    model = Category  # type: ignore  # noqa: PGH003
    search_fields = ("name",)
    # Display submit button in filters
    list_filter_submit = True

    list_filter = (
        CustomTextFilter,
        CustomDropdownFilter,
        "name",
    )

    list_display = ("name",)
    inlines = [ComicInline]

    # Display changelist in fullwidth
    list_fullwidth = False

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail
    actions = []
    import_form_class = ImportForm
    export_form_class = ExportForm
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        ArrayField: {
            "widget": ArrayWidget,
        },
    }


@admin.register(Author)
class AuthorAdminClass(ModelAdmin, ImportExportModelAdmin):
    # Display fields in changeform in compressed mode
    compressed_fields = True  # Default: False

    # Warn before leaving unsaved changes in changeform
    warn_unsaved_form = True  # Default: False

    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }
    model = Author  # type: ignore  # noqa: PGH003
    search_fields = (
        CustomTextFilter,
        CustomDropdownFilter,
        "name",
    )  # type: ignore  # noqa: PGH003
    # Display submit button in filters
    list_filter_submit = True

    list_filter = ("name",)

    list_display = ("name",)
    inlines = [ComicInline]

    # Display changelist in fullwidth
    list_fullwidth = False

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail
    actions = []
    import_form_class = ImportForm
    export_form_class = ExportForm
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        ArrayField: {
            "widget": ArrayWidget,
        },
    }


@admin.register(Artist)
class ArtistAdminClass(ModelAdmin, ImportExportModelAdmin):
    # Display fields in changeform in compressed mode
    compressed_fields = True  # Default: False

    # Warn before leaving unsaved changes in changeform
    warn_unsaved_form = True  # Default: False

    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }
    model = Artist  # type: ignore  # noqa: PGH003
    search_fields = ("name",)
    # Display submit button in filters
    list_filter_submit = True

    list_filter = (
        CustomTextFilter,
        CustomDropdownFilter,
        "name",
    )

    list_display = ("name",)
    inlines = [ComicInline]

    # Display changelist in fullwidth
    list_fullwidth = False

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail
    actions = []
    import_form_class = ImportForm
    export_form_class = ExportForm
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        ArrayField: {
            "widget": ArrayWidget,
        },
    }


@admin.register(Comment)
class CommentAdminClass(ModelAdmin, ImportExportModelAdmin):
    # Display fields in changeform in compressed mode
    compressed_fields = True  # Default: False

    # Warn before leaving unsaved changes in changeform
    warn_unsaved_form = True  # Default: False

    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }
    model = Comment  # type: ignore  # noqa: PGH003
    search_fields = ("text",)
    # Display submit button in filters
    list_filter_submit = True

    list_filter = (
        CustomTextFilter,
        CustomDropdownFilter,
        "text",
        ("created_at", RangeDateTimeFilter),
    )

    list_display = ("text",)
    inlines = []

    # Display changelist in fullwidth
    list_fullwidth = False

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail
    actions = []
    import_form_class = ImportForm
    export_form_class = ExportForm
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        ArrayField: {
            "widget": ArrayWidget,
        },
    }


@admin.register(Website)
class WebsiteAdminClass(ModelAdmin, ImportExportModelAdmin):
    # Display fields in changeform in compressed mode
    compressed_fields = True  # Default: False

    # Warn before leaving unsaved changes in changeform
    warn_unsaved_form = True  # Default: False

    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }
    model = Website  # type: ignore  # noqa: PGH003
    search_fields = ("name",)
    # Display submit button in filters
    list_filter_submit = True

    list_filter = (
        CustomTextFilter,
        CustomDropdownFilter,
        "name",
    )

    list_display = ("name",)
    inlines = []

    # Display changelist in fullwidth
    list_fullwidth = False

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail
    actions = []
    import_form_class = ImportForm
    export_form_class = ExportForm
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        ArrayField: {
            "widget": ArrayWidget,
        },
    }


@admin.register(UserComic)
class UserComicAdminClass(ModelAdmin, ImportExportModelAdmin):
    # Display fields in changeform in compressed mode
    compressed_fields = True  # Default: False

    # Warn before leaving unsaved changes in changeform
    warn_unsaved_form = True  # Default: False

    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }
    model = UserComic  # type: ignore  # noqa: PGH003
    search_fields = (
        "comic",
        "user",
    )
    # Display submit button in filters
    list_filter_submit = True

    list_filter = (
        CustomTextFilter,
        CustomDropdownFilter,
        "comic",
        "user",
    )

    list_display = (
        "comic",
        "user",
    )
    inlines = []

    # Display changelist in fullwidth
    list_fullwidth = False

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail
    actions = []
    import_form_class = ImportForm
    export_form_class = ExportForm
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        ArrayField: {
            "widget": ArrayWidget,
        },
    }
