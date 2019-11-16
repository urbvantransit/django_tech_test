from marshmallow import Schema, fields

class LineSchema(Schema):
    id = fields.String()
    name = fields.String()
    color = fields.String()