from marshmallow import Schema, fields


class LineSchema(Schema):
    """
        id - Unique identifier of the line
        name - Name of the line
        color - Color of the line
    """
    id = fields.String()
    name = fields.String()
    color = fields.String()


class RouterSchema(Schema):
    """
        id - Unique identifier of the route
        lines - Lines of the route
        direction - Shows direction of the route
        is_active - Indicates if the route is active
    """
    id = fields.String()
    lines = fields.String()
    direction = fields.Boolean()
    is_active = fields.Boolean()
