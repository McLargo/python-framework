from datetime import date

from dateutil.relativedelta import relativedelta
from marshmallow import INCLUDE, Schema, fields, validate


class DemoSchema(Schema):
    class Meta:
        unknown = INCLUDE

    first_name = fields.String(validate=validate.Length(max=128), required=True)
    last_name = fields.String(validate=validate.Length(max=128), required=True)
    born = fields.Date(required=True)
    died = fields.Date(allow_none=True, missing=None)
    age = fields.Method("get_age")
    alive = fields.Method("is_alive")

    def get_age(self, instance):
        died = instance.get("died")
        if died is None:
            died = date.today()
        return relativedelta(died, instance["born"]).years

    def is_alive(self, instance):
        return instance.get("died") is None
