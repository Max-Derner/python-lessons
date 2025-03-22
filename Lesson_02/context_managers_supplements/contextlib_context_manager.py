from datetime import timedelta, datetime
from contextlib import contextmanager

from robolib import (
    initialise_data_channel,
    DataCollection,
    collect_data,
    transmit_data,
)


@contextmanager
def my_context_manager(transmission_period: timedelta = timedelta(weeks=8)):
    # initialisation here
    data_store = DataCollection()
    data_store.transmission_period = transmission_period
    # __enter__ style code here
    initialise_data_channel()
    try:
        yield data_store
    # __exit__ style code here
    except KeyboardInterrupt as e:
        print(F"An issue has arisen! {type(e)}")
        print("Conducting emergency transmission of remaining data...")
    except Exception as e:
        print(F"An issue has arisen! {type(e)}")
        print("Conducting emergency transmission of remaining data...")
        raise
    else:
        print("Sending remaining data...")
    finally:
        transmit_data(data_store.format_for_transmission())
        print("sent")


def main():
    last_data_collection = datetime.now()
    collection_period = timedelta(seconds=0.5)
    with my_context_manager(transmission_period=timedelta(seconds=5)) as d:
        pass
    with my_context_manager(
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
