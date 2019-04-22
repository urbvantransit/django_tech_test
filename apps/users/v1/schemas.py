from marshmallow import (Schema, fields)


class UserSchema(Schema):

    id = fields.String()
    username = fields.String()
    password = fields.String()
    is_tier2 = fields.Boolean()
    is_tier2 = fields.Boolean()
    is_staff = fields.Boolean()
    is_superuser = fields.Boolean()
    is_active = fields.Boolean()
    date_joined = fields.DateTime()
