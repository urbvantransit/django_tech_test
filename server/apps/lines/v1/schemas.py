# coding: utf-8
from marshmallow import Schema
from marshmallow.fields import Bool, Method, Nested, String

from apps.lines.models import RouteModel
from apps.stations.v1.schemas import StationSchema


class LineSchema(Schema):

    id = String()
    name = String()
    color = String()


class RouteSchema(Schema):

    id = String()
    line = Nested(LineSchema)
    stations = Method('get_stations')
    direction = Bool()
    is_active = Bool()

    def get_stations(self, instance):
        stations = instance.stations.all()
        return StationSchema(many=True).dump(stations).data

    