import jsonschema

from demoapp.exceptions import ValidationException


def validate_schema(schema, data):
    # validates if data matches with corresponding schema
    try:
        jsonschema.Draft4Validator.check_schema(schema=schema)
        return jsonschema.Draft4Validator(schema).validate(data) is None
    except jsonschema.ValidationError as error:
        raise ValidationException("Validation: {}".format(error.message))
