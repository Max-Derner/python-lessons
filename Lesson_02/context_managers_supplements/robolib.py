from datetime import datetime, timedelta
from uuid import uuid4


DATA_CHANNEL = "data_transmission.txt"  # just play along


def initialise_data_channel():
    with open(DATA_CHANNEL, mode='w') as chan:
        chan.write('')


def transmit_data(data):
    with open(DATA_CHANNEL, mode='a') as chan:
        chan.write(data)


def collect_data() -> str:
    return uuid4()  # play along here too


class DataCollection:

    transmission_period = timedelta(weeks=8)

    def __init__(self):
        self.data = []

    def commit_record(self, message: str):
        self.data.append(
            (datetime.now(), message)
        )

    def reset(self):
        self.data = []

    @property
    def data_due_to_send(self):
        if len(self.data) == 0:
            return False
        self.data.sort()
        oldest_data_point = self.data[0]
        current_time = datetime.now()
        oldest_time = oldest_data_point[0]
        age_of_oldest_data = current_time - oldest_time
        if age_of_oldest_data >= self.transmission_period:
            return True
        else:
            return False

    def format_for_transmission(self):
        self.data.sort()
        output = (
            '   ==================== '
            'TRANSMISSION START'
            ' ====================  \n'
        )
        for time, message in self.data:
            output += F"[{time}] {message}\n"
        output += (
            '   ====================  '
            'TRANSMISSION END'
            '  ====================  \n'
        )
        return output
