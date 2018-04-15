# coding: utf8
from rest_framework import pagination
from rest_framework.response import Response

from marshmallow import (Schema, fields, pre_dump)


class BaseErrorSchema(Schema):

    code = fields.Integer()
    message = fields.String()
    field = fields.String()
    app = fields.String()


class BaseBodyLinkSchema(Schema):

    next = fields.String(default=None)
    previous = fields.String(default=None)


class BaseBodySchema(Schema):

    links = fields.Nested(
        BaseBodyLinkSchema(),
        default=BaseBodyLinkSchema().dump({}).data
    )
    count = fields.Integer()
    results = fields.List(fields.Dict())

    @pre_dump
    def validate_count(self, data):

        count = len(data.get("results", []))
        data['count'] = count

        return data


class BaseResponseSchema(Schema):

    errors = fields.Nested(BaseErrorSchema, many=True, default=[])
    body = fields.Nested(BaseBodySchema, default={})


class PaginationResponse(pagination.PageNumberPagination):

    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'body': {
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'count': self.page.paginator.count,
                'results': data
            },
            'errors': []
        })
