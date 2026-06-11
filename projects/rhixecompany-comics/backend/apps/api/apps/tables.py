import django_tables2 as tables
from django.conf import settings
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from api.apps.models import Chapter
from api.apps.models import Comic
from api.users.models import User


class MaterializeCssCheckboxColumn(tables.CheckBoxColumn):
    def render(self, value, bound_column, record):
        default = {"type": "checkbox", "name": bound_column.name, "value": value}
        if self.is_checked(value, record):
            default.update({"checked": "checked"})
        general = self.attrs.get("input")
        specific = self.attrs.get("td__input")
        attrs = tables.utils.AttributeDict(default, **(specific or general or {}))
        html = (
            f'<label class="flex items-center cursor-pointer text-neutral-600 dark:text-neutral-300"><div class="relative flex items-center"><input {attrs.as_html()} class="before:content['  # noqa: E501
            '] peer relative size-4 cursor-pointer appearance-none overflow-hidden rounded border border-neutral-300 bg-white before:absolute before:inset-0 checked:border-black checked:before:bg-black focus:outline focus:outline-2 focus:outline-offset-2 focus:outline-neutral-800 checked:focus:outline-black active:outline-offset-0 dark:border-neutral-700 dark:bg-neutral-900 dark:checked:border-white dark:checked:before:bg-white dark:focus:outline-neutral-300 dark:checked:focus:outline-white"  :checked="checkAll" /><svg xmlns="http://www.w3.org/2000/svg"viewBox="0 0 24 24"aria-hidden="true"stroke="currentColor"fill="none"stroke-width="4"class="pointer-events-none invisible absolute left-1/2 top-1/2 size-3 -translate-x-1/2 -translate-y-1/2 text-neutral-100 peer-checked:visible dark:text-black"><path stroke-linecap="round"stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5" ></svg></div></label>'  # noqa: E501
        )
        return mark_safe(html)  # noqa: S308


class ComicTable(tables.Table):
    id = MaterializeCssCheckboxColumn(orderable=True)
    comic = tables.TemplateColumn(
        orderable=True,
        template_name="partials/comics/table_comic.html",
    )
    actions = tables.TemplateColumn(
        orderable=True,
        template_name="partials/comics/table_actions.html",
    )

    updated_at = tables.DateColumn(orderable=True, format=settings.FORMAT)

    class Meta:
        model = Comic
        sequence = (
            "id",
            "comic",
            "status",
            "type",
            "updated_at",
            "actions",
        )
        fields = (
            "id",
            "comic",
            "status",
            "type",
            "updated_at",
            "actions",
        )
        template_name = "partials/comics/custom_table.html"
        attrs = {
            "class": "mytable",
            "td": {
                "class": "mytablecol",
            },
            "th": {
                "_ordering": {
                    "orderable": "sortable",  # Instead of `orderable`
                    "ascending": "ascend",  # Instead of `asc`
                    "descending": "descend",  # Instead of `desc`
                },
            },
        }
        row_attrs = {"id": lambda record: record.pk, "class": "mytablerow"}

    def render_status(self, value):
        if value == "Completed":
            return format_html(
                "<span class='mr-2 rounded-md border border-green-100 bg-green-100 px-2.5 py-0.5 text-xs font-medium text-green-800 dark:border-green-500 dark:bg-gray-700 dark:text-green-400'>{}</span>",  # noqa: E501
                value,
            )
        if value == "Dropped":
            return format_html(
                "<span class='mr-2 rounded-md border border-red-100 bg-red-100 px-2.5 py-0.5 text-xs font-medium text-red-800 dark:border-red-500 dark:bg-gray-700 dark:text-red-400'>{}</span>",  # noqa: E501
                value,
            )
        if value == "Hiatus":
            return format_html(
                "<span class='mr-2 rounded-md border border-blue-100 bg-blue-100 px-2.5 py-0.5 text-xs font-medium text-blue-800 dark:border-blue-500 dark:bg-gray-700 dark:text-blue-400'>{}</span>",  # noqa: E501
                value,
            )
        if value == "Season End":
            return format_html(
                "<span class='mr-2 rounded-md border border-orange-100 bg-orange-100 px-2.5 py-0.5 text-xs font-medium text-orange-800 dark:border-orange-500 dark:bg-gray-700 dark:text-orange-400'>{}</span>",  # noqa: E501
                value,
            )
        if value == "Coming Soon":
            return format_html(
                "<span class='mr-2 rounded-md border border-violet-100 bg-violet-100 px-2.5 py-0.5 text-xs font-medium text-violet-800 dark:border-violet-500 dark:bg-gray-700 dark:text-violet-400'>{}</span>",  # noqa: E501
                value,
            )
        return format_html(
            "<span class='mr-2 rounded-md border border-purple-100 bg-purple-100 px-2.5 py-0.5 text-xs font-medium text-purple-800 dark:border-purple-500 dark:bg-gray-700 dark:text-purple-400'>{}</span>",  # noqa: E501
            value,
        )


class ChapterTable(tables.Table):
    id = MaterializeCssCheckboxColumn(orderable=True)
    chapter = tables.TemplateColumn(
        orderable=True,
        template_name="partials/chapters/table_chapter.html",
    )
    actions = tables.TemplateColumn(
        orderable=True,
        template_name="partials/chapters/table_actions.html",
    )
    updated_at = tables.DateColumn(orderable=True, format=settings.FORMAT)

    class Meta:
        model = Chapter
        sequence = (
            "id",
            "chapter",
            "numpages",
            "updated_at",
            "actions",
        )
        fields = (
            "id",
            "chapter",
            "numpages",
            "updated_at",
            "actions",
        )
        template_name = "partials/chapters/custom_table.html"
        attrs = {
            "class": "mytable",
            "td": {
                "class": "mytablecol",
            },
            "th": {
                "_ordering": {
                    "orderable": "sortable",  # Instead of `orderable`
                    "ascending": "ascend",  # Instead of `asc`
                    "descending": "descend",  # Instead of `desc`
                },
            },
        }
        row_attrs = {"data-id": lambda record: record.pk, "class": "mytablerow"}


class UserTable(tables.Table):
    id = MaterializeCssCheckboxColumn(orderable=True)
    user = tables.TemplateColumn(
        orderable=True,
        template_name="partials/users/table_user.html",
    )
    actions = tables.TemplateColumn(
        orderable=True,
        template_name="partials/users/table_actions.html",
    )

    class Meta:
        model = User
        sequence = (
            "id",
            "user",
            "is_active",
            "actions",
        )
        fields = (
            "id",
            "user",
            "is_active",
            "actions",
        )
        template_name = "partials/users/custom_table.html"
        attrs = {
            "class": "mytable",
            "td": {
                "class": "mytablecol",
            },
            "th": {
                "_ordering": {
                    "orderable": "sortable",  # Instead of `orderable`
                    "ascending": "ascend",  # Instead of `asc`
                    "descending": "descend",  # Instead of `desc`
                },
            },
        }
        row_attrs = {"data-id": lambda record: record.pk, "class": "mytablerow"}

    def render_is_active(self, value):
        if value is False:
            return format_html(
                "<div class='flex items-center'><div class='h-2.5 w-2.5 rounded-full bg-red-500 mr-2'></div>{}</div>",  # noqa: E501
                value,
            )

        return format_html(
            "<div class='flex items-center'><div class='h-2.5 w-2.5 rounded-full bg-green-400 mr-2'></div>{}</div>",  # noqa: E501
            value,
        )
