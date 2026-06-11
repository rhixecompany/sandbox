from allauth.account.decorators import secure_admin_login
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.postgres.fields import ArrayField
from django.core.validators import EMPTY_VALUES
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_celery_beat.admin import ClockedScheduleAdmin as BaseClockedScheduleAdmin
from django_celery_beat.admin import CrontabScheduleAdmin as BaseCrontabScheduleAdmin
from django_celery_beat.admin import PeriodicTaskAdmin as BasePeriodicTaskAdmin
from django_celery_beat.admin import PeriodicTaskForm
from django_celery_beat.admin import TaskSelectWidget
from django_celery_beat.models import ClockedSchedule
from django_celery_beat.models import CrontabSchedule
from django_celery_beat.models import IntervalSchedule
from django_celery_beat.models import PeriodicTask
from django_celery_beat.models import SolarSchedule
from import_export.admin import ImportExportModelAdmin
from import_export.forms import ExportForm
from import_export.forms import ImportForm
from unfold.admin import ModelAdmin
from unfold.contrib.filters.admin import DropdownFilter
from unfold.contrib.filters.admin import TextFilter
from unfold.contrib.forms.widgets import ArrayWidget
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.forms import AdminPasswordChangeForm
from unfold.widgets import UnfoldAdminSelectWidget
from unfold.widgets import UnfoldAdminTextInputWidget

from api.users.forms import UserAdminChangeForm
from api.users.forms import UserAdminCreationForm
from api.users.models import User

admin.site.index_title = "Welcome to the Rhixescans admin area"
admin.site.site_header = "Rhixescans Admin"
admin.site.site_title = "Rhixescans Admin Area"

if settings.DJANGO_ADMIN_FORCE_ALLAUTH:
    # Force the `admin` sign in process to go through the `django-allauth` workflow:
    # https://docs.allauth.org/en/latest/common/admin.html#admin
    admin.autodiscover()
    admin.site.login = secure_admin_login(admin.site.login)  # type: ignore[method-assign]


class UnfoldTaskSelectWidget(UnfoldAdminSelectWidget, TaskSelectWidget):
    pass


class UnfoldPeriodicTaskForm(PeriodicTaskForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["task"].widget = UnfoldAdminTextInputWidget()
        self.fields["regtask"].widget = UnfoldTaskSelectWidget()


class CustomDropdownFilter(DropdownFilter):
    title = _("Custom dropdown filter")
    parameter_name = "query_param_in_uri"

    def lookups(self, request, model_admin):
        return [
            ["option_1", _("Option 1")],
            ["option_2", _("Option 2")],
        ]

    def queryset(self, request, queryset):
        if self.value() not in EMPTY_VALUES:
            # Here write custom query
            return queryset.filter(your_field=self.value())

        return queryset


class CustomTextFilter(TextFilter):
    title = _("Custom filter")
    parameter_name = "query_param_in_uri"

    def queryset(self, request, queryset):
        if self.value() not in EMPTY_VALUES:
            # Here write custom query
            return queryset.filter(your_field=self.value())

        return queryset


@admin.register(User)
class UserAdminClass(ModelAdmin, ImportExportModelAdmin, auth_admin.UserAdmin):
    # Display fields in changeform in compressed mode
    compressed_fields = True  # Default: False

    # Warn before leaving unsaved changes in changeform
    warn_unsaved_form = True  # Default: False

    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }
    model = User
    search_fields = (
        "email",
        "username",
        "first_name",
    )
    ordering = ["id"]
    # Display submit button in filters
    list_filter_submit = True

    list_filter = (
        CustomTextFilter,
        CustomDropdownFilter,
        "email",
        "username",
        "first_name",
    )

    list_display = (
        "email",
        "username",
        "first_name",
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
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    change_password_form = AdminPasswordChangeForm
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
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("username",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.unregister(PeriodicTask)
admin.site.unregister(IntervalSchedule)
admin.site.unregister(CrontabSchedule)
admin.site.unregister(SolarSchedule)
admin.site.unregister(ClockedSchedule)


@admin.register(PeriodicTask)
class PeriodicTaskAdmin(BasePeriodicTaskAdmin, ModelAdmin):
    form = UnfoldPeriodicTaskForm


@admin.register(IntervalSchedule)
class IntervalScheduleAdmin(ModelAdmin):
    pass


@admin.register(CrontabSchedule)
class CrontabScheduleAdmin(BaseCrontabScheduleAdmin, ModelAdmin):
    pass


@admin.register(SolarSchedule)
class SolarScheduleAdmin(ModelAdmin):
    pass


@admin.register(ClockedSchedule)
class ClockedScheduleAdmin(BaseClockedScheduleAdmin, ModelAdmin):
    pass
