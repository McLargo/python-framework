from datetime import date, datetime

from dateutil.relativedelta import relativedelta


class DemoSerializer:
    def instance(self):
        # TODO: this will fetch info from database, redis, file...
        return {
            "first_name": "Nelson",
            "last_name": "Mandela",
            "born": datetime(1918, 7, 18),
            "died": datetime(2013, 12, 15),
        }

    @staticmethod
    def calculate_age(start_date, end_date):
        if end_date is None:
            end_date = date.today()
        return relativedelta(end_date, start_date).years

    def response(self, instance=None):
        if instance is None:
            instance = self.instance()
        return {
            "full_name": f"{instance['first_name']} {instance['last_name']}",
            "age": DemoSerializer.calculate_age(
                instance["born"], instance["died"]
            ),
            "is_alive": instance["died"] is None,
        }
