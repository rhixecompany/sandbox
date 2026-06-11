from django.core.validators import EMPTY_VALUES
from django.utils.translation import gettext_lazy as _
from django_celery_beat.admin import PeriodicTaskForm
from django_celery_beat.admin import TaskSelectWidget
from unfold.contrib.filters.admin import DropdownFilter
from unfold.contrib.filters.admin import TextFilter
from unfold.widgets import UnfoldAdminSelectWidget
from unfold.widgets import UnfoldAdminTextInputWidget


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
