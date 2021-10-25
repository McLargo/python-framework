from datetime import datetime


class DemoDeserializer:

    @staticmethod
    def deserializer(data):
        # TODO: ugly deserializer, can be customize with factory
        response = {}
        if "middle_name" in data:
            response["first_name"] = f"{data['first_name']} {data['middle_name']}"
        else:
            response["first_name"] = data["first_name"]
        response["last_name"] = data["last_name"]
        response["born"] = datetime.strptime(data["dob"], "%d-%m-%Y")
        if "dead" not in response:
            response["died"] = None
        return response
