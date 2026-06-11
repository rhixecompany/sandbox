from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = "page_size"
    max_page_size = 10000

    def get_paginated_response(self, data):
        return Response(
            {
                "next_page": self.get_next_link(),
                "previous_page": self.get_previous_link(),
                "total_results": self.page.paginator.count,  # type: ignore  # noqa: PGH003
                "total_pages": self.page.paginator.num_pages,  # type: ignore  # noqa: PGH003
                "results": data,
            },
        )


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = "page_size"
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(
            {
                "next_page": self.get_next_link(),
                "previous_page": self.get_previous_link(),
                "total_results": self.page.paginator.count,  # type: ignore  # noqa: PGH003
                "total_pages": self.page.paginator.num_pages,  # type: ignore  # noqa: PGH003
                "results": data,
            },
        )
