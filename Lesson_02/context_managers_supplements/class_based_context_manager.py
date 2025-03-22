from datetime import timedelta, datetime

from robolib import (
    initialise_data_channel,
    DataCollection,
    collect_data,
    transmit_data,
)


class MyContextManager:

    def __init__(
            self,
            transmission_period: timedelta = timedelta(weeks=8),
    ):
        self.data_store = DataCollection()
        self.data_store.transmission_period = transmission_period

    def __enter__(self) -> DataCollection:
        initialise_data_channel()
        return self.data_store

    def __exit__(self, exc_type, exc_value, traceback):
        # you may inspect these values 'exc_type', 'exc_value', and
        # 'traceback' to determine the error and whether an error has
        # happened to suppress and whether to reraise the exception
        if exc_type is not None:
            print(F"An issue has arisen! {exc_type}")
            print("Conducting emergency transmission of remaining data...")
        else:
            print("Sending remaining data...")
        transmit_data(self.data_store.format_for_transmission())
        print("sent")
        # return a boolean to indicate whether or not you are
        # suppressing the exception
        return True if exc_type == KeyboardInterrupt else False


def main():
    last_data_collection = datetime.now()
    collection_period = timedelta(seconds=0.5)
    with MyContextManager(transmission_period=timedelta(seconds=5)) as d:
        pass
    with MyContextManager(
        transmission_period=timedelta(seconds=5),
    ) as data_store:
        while True:
            current_time = datetime.now()
            time_since_last_collection = current_time - last_data_collection
            if time_since_last_collection >= collection_period:
                print("Collecting data")
                data = collect_data()
                last_data_collection += collection_period
                data_store.commit_record(data)
                print("collected")
            if data_store.data_due_to_send:
                print("Sending data")
                transmit_data(data_store.format_for_transmission())
                data_store.reset()
                print("sent")

    # You will only see this if the context manager
    # suppresses the exception
    print("a graceful end")


if __name__ == "__main__":
    main()
