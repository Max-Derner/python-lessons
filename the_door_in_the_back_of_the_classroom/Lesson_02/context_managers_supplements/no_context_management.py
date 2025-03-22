from datetime import datetime, timedelta

from robolib import (
    initialise_data_channel,
    DataCollection,
    collect_data,
    transmit_data,
)


def main():
    initialise_data_channel()
    data_store = DataCollection()
    # For this example we'll bring the transmission period down to only
    # 5 seconds and set the program to gather data every 0.5 seconds.
    data_store.transmission_period = timedelta(seconds=5)
    collection_period = timedelta(seconds=0.5)
    last_data_collection = datetime.now()
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
            print("Sending data...")
            transmit_data(data_store.format_for_transmission())
            data_store.reset()
            print("sent")


if __name__ == "__main__":
    main()
