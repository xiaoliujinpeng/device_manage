from rest_framework import pagination
from rest_framework.response import Response
from collections import OrderedDict


class PageSet(pagination.PageNumberPagination):
    page_size = 10
    page_query_param = "size"
    max_page_size = 100
    page_query_param = "page"

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ("page", self.page.number),
            ("count", self.page.paginator.count),
            ("next", self.get_next_link()),
            ("previous", self.get_previous_link()),
            ("results", data),
        ]))
