# coding: utf8
from marshmallow import (Schema, fields)


class UserSchema(Schema):

    id = fields.String()
    username = fields.String()
    email = fields.String()
    first_name = fields.String()
    last_name = fields.String()

