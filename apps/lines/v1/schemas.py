from marshmallow import (Schema, fields)

from apps.stations.v1.schemas import StationSchema


class LineSchema(Schema):
    id = fields.String()
    name = fields.String()
    color = fields.String()


class RouteSchema(Schema):
    id = fields.String()
    line = fields.Nested(LineSchema)
    stations = fields.Method('get_all_stations')
    direction = fields.Boolean()
    is_active = fields.Boolean()

    def get_all_stations(self, instance):
        '''
        Get all available stations
        '''
        stations = instance.stations.all()
        schema = StationSchema(many=True).dump(stations)
        return schema.data