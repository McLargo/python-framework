schema_request = {
    "title": "Request accepted",
    "type": "object",
    "required": ["first_name", "last_name", "dob"],
    "properties": {
        "first_name": {"description": "first name", "type": "string"},
        "middle_name": {"description": "middle name", "type": "string"},
        "last_name": {"description": "last name", "type": "string"},
        "dob": {"description": "date of birth", "type": "string"},
    },
}


schema_response = {
    "title": "Response accepted",
    "type": "array",
    "items": {
        "type": "object",
        "required": ["name", "p"],
        "properties": {
            "name": {
                "description": "Name of powerplant",
                "type": "string",
            },
            "p": {
                "description": "P produce by the powerplant",
                "type": "number",
            },
        },
    },
}
