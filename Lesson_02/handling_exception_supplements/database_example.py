from traceback import print_exception
from uuid import uuid4
from database import (
    InvalidDataError,
    ClientError,
    DatabaseError,
    validate_data,
    start_database_session,
    put_data,
)


class PutDataError(Exception):
    """An exception raised by the put_data method upon failure"""


def put_record(data):
    """Places record in table, if record already exists an exception is
    raised as you should use the update function.

    Database schema:

    `id`: uuid4, `name`: str, `phone_no`: str & '\\+\\d{12}'

    Not all fields required, but all fields must conform to expected
    datatype."""

    exp = PutDataError(F"Failed to put data: {data}")

    try:
        validate_data(data)
    except InvalidDataError as e:
        raise exp from e

    try:
        session = start_database_session()
    except ClientError as e:
        raise exp from e

    try:
        response = put_data(session, data)
    except DatabaseError as e:
        raise exp from e

    print(F"{response=}")


if __name__ == "__main__":
    id1 = str(uuid4())
    id2 = str(uuid4())
    id3 = str(uuid4())
    all_data = [
        {'id': id1, 'name': 'mark',
         'phone_no': (
             'plus forty four, seven seven oh nine eight five two two eight'
         )},
        {'id': id2, 'name': 'max', 'phone_no': '+447709852336'},
        {'id': id3, 'name': 'mike', 'phone_no': '+447709852456'},
        {'id': id3, 'name': 'marvin', 'phone_no': '+447097563436'},
    ]

    def display_data(data: list):
        for i, d in enumerate(data):
            print(F"{i}: {d}")

    selection = None
    while selection != 'e':
        display_data(all_data)
        selection = input(
            "Choose an item to place in the "
            "database or choose 'e' to exit: "
        )
        try:
            item = all_data[int(selection)]
        except (ValueError, IndexError):
            pass
        else:
            try:
                put_record(item)
            except PutDataError as e:
                print("Exception occurred!\n\n")
                print_exception(e)
                print("\n")
