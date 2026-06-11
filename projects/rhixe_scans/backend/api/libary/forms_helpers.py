from django import forms
from django.forms.widgets import ChoiceWidget
from django.utils.translation import gettext_lazy as _

FILE_INPUT_CONTRADICTION = object()


class MyDateInput(forms.widgets.DateTimeBaseInput):
    input_type = "date"
    format_key = "DATE_INPUT_FORMATS"
    template_name = "partials/widgets/date.html"


class MyRadioSelect(ChoiceWidget):
    input_type = "radio"
    template_name = "partials/widgets/radio.html"
    option_template_name = "partials/widgets/radio_option.html"
    use_fieldset = True

    def id_for_label(self, id_, index=None):
        """
        Don't include for="field_0" in <label> to improve accessibility when
        using a screen reader, in addition clicking such a label would toggle
        the first input.
        """
        if index is None:
            return ""
        return super().id_for_label(id_, index)


class MyMulRadioSelect(forms.RadioSelect):
    allow_multiple_selected = True
    input_type = "checkbox"
    template_name = "partials/widgets/radio.html"
    option_template_name = "partials/widgets/radio_option.html"

    def use_required_attribute(self, initial):
        # Don't use the 'required' attribute because browser validation would
        # require all checkboxes to be checked instead of at least one.
        return False

    def value_omitted_from_data(self, data, files, name):
        # HTML checkboxes don't appear in POST data if not checked, so it's
        # never known if the value is actually omitted.
        return False


class MyCustomImageWidget(forms.ClearableFileInput):
    clear_checkbox_label = _("Clear")  # type: ignore  # noqa: PGH003
    initial_text = _("Currently")  # type: ignore  # noqa: PGH003
    input_text = _("Change")  # type: ignore  # noqa: PGH003
    help_text = _("SVG, PNG, JPG or GIF (MAX. 800x400px).")
    template_name = "partials/widgets/custom_image_widget.html"
    checked = False

    def clear_checkbox_name(self, name):
        """
        Given the name of the file input, return the name of the clear checkbox
        input.
        """
        return name + "-clear"

    def clear_checkbox_id(self, name):
        """
        Given the name of the clear checkbox input, return the HTML id for it.
        """
        return name + "_id"

    def is_initial(self, value):
        """
        Return whether value is considered to be initial value.
        """
        return bool(value and getattr(value, "url", False))

    def format_value(self, value):
        """
        Return the file object if it has a defined url attribute.
        """
        if self.is_initial(value):
            return value
        return None

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        checkbox_name = self.clear_checkbox_name(name)
        checkbox_id = self.clear_checkbox_id(checkbox_name)
        context["widget"].update(
            {
                "help_text": self.help_text,
                "checkbox_name": checkbox_name,
                "checkbox_id": checkbox_id,
                "is_initial": self.is_initial(value),
                "input_text": self.input_text,
                "initial_text": self.initial_text,
                "clear_checkbox_label": self.clear_checkbox_label,
            },
        )
        context["widget"]["attrs"].setdefault("disabled", False)
        context["widget"]["attrs"]["checked"] = self.checked
        return context

    def value_from_datadict(self, data, files, name):
        upload = super().value_from_datadict(data, files, name)
        self.checked = self.clear_checkbox_name(name) in data
        if not self.is_required and forms.CheckboxInput().value_from_datadict(
            data,
            files,
            self.clear_checkbox_name(name),
        ):
            if upload:
                # If the user contradicts themselves (uploads a new file AND
                # checks the "clear" checkbox), we return a unique marker
                # object that FileField will turn into a ValidationError.
                return FILE_INPUT_CONTRADICTION
            # False signals to clear any existing value, as opposed to just None
            return False
        return upload

    def value_omitted_from_data(self, data, files, name):
        return (
            super().value_omitted_from_data(data, files, name)
            and self.clear_checkbox_name(name) not in data
        )


class MyCheckboxSelectMultiple(forms.RadioSelect):
    allow_multiple_selected = True
    input_type = "checkbox"
    template_name = "partials/widgets/checkbox_select.html"
    option_template_name = "partials/widgets/checkbox_option.html"
    # template_name = "django/forms/widgets/checkbox_select.html" # noqa: ERA001
    # option_template_name = "django/forms/widgets/checkbox_option.html" # noqa: ERA001

    def use_required_attribute(self, initial):
        # Don't use the 'required' attribute because browser validation would
        # require all checkboxes to be checked instead of at least one.
        return False

    def value_omitted_from_data(self, data, files, name):
        # HTML checkboxes don't appear in POST data if not checked, so it's
        # never known if the value is actually omitted.
        return False


class MyAdminCheckboxSelectMultiple(forms.RadioSelect):
    allow_multiple_selected = True
    input_type = "checkbox"
    template_name = "partials/widgets/checkbox_select2.html"
    option_template_name = "partials/widgets/checkbox_option2.html"
    # template_name = "django/forms/widgets/checkbox_select.html" # noqa: ERA001
    # option_template_name = "django/forms/widgets/checkbox_option.html" # noqa: ERA001

    def use_required_attribute(self, initial):
        # Don't use the 'required' attribute because browser validation would
        # require all checkboxes to be checked instead of at least one.
        return False

    def value_omitted_from_data(self, data, files, name):
        # HTML checkboxes don't appear in POST data if not checked, so it's
        # never known if the value is actually omitted.
        return False
