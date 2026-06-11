import django_tables2 as tables
from django.utils.safestring import mark_safe

from api.libary.models import Chapter
from api.libary.models import Comic


class MaterializeCssCheckboxColumn(tables.CheckBoxColumn):
    def render(self, value, bound_column, record):
        default = {"type": "checkbox", "name": bound_column.name, "value": value}
        if self.is_checked(value, record):
            default.update({"checked": "checked"})
        general = self.attrs.get("input")
        specific = self.attrs.get("td__input")
        attrs = tables.utils.AttributeDict(default, **(specific or general or {}))
        html = f'<div class="flex items-center"><input {attrs.as_html()} class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" /><label class="sr-only"></label></div>'  # noqa: E501
        return mark_safe(html)  # noqa: S308


class ComicTable(tables.Table):
    id = MaterializeCssCheckboxColumn(orderable=True)
    comic = tables.TemplateColumn(
        orderable=True,
        template_name="partials/comics/table_comic.html",
    )
    actions = tables.TemplateColumn(
        orderable=False,
        template_name="partials/comics/table_actions.html",
    )
    updated_at = tables.DateColumn(orderable=True)

    class Meta:
        model = Comic
        sequence = (
            "id",
            "comic",
            "status",
            "updated_at",
            "actions",
        )
        fields = (
            "id",
            "comic",
            "updated_at",
            "status",
            "actions",
        )
        template_name = "partials/comics/custom_table.html"
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",  # Instead of `orderable`
                    "ascending": "ascend",  # Instead of `asc`
                    "descending": "descend",  # Instead of `desc`
                },
            },
        }


class ChapterTable(tables.Table):
    id = MaterializeCssCheckboxColumn(orderable=True)
    chapter = tables.TemplateColumn(
        orderable=True,
        template_name="partials/chapters/table_chapter.html",
    )
    actions = tables.TemplateColumn(
        orderable=False,
        template_name="partials/chapters/table_actions.html",
    )
    updated_at = tables.DateColumn(orderable=True)

    class Meta:
        model = Chapter
        sequence = (
            "id",
            "chapter",
            "numimages",
            "updated_at",
            "actions",
        )
        fields = (
            "id",
            "chapter",
            "updated_at",
            "numimages",
            "actions",
        )
        template_name = "partials/chapters/custom_table.html"
        attrs = {
            "th": {
                "_ordering": {
                    "orderable": "sortable",  # Instead of `orderable`
                    "ascending": "ascend",  # Instead of `asc`
                    "descending": "descend",  # Instead of `desc`
                },
            },
        }
