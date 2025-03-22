import re
from uuid import uuid4


class InvalidDataError(Exception):
    """raised by validate_data when teh data is invalid"""


def validate_data(data: dict):
    if not isinstance(data, dict):
        raise InvalidDataError('data is not dict')
    errors = []
    if not isinstance((id := data.get('id')), str):
        errors.append(F"id should be type string got {type(id)}")
    else:
        id_pattern = (
            r'[0-9a-f]{8}'
            r'-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}'
            r'-[0-9a-f]{12}'
        )
        match = re.match(
            id_pattern,
            id,
        )
        if not match:
            errors.append(F"id did not match the RegEx {id_pattern}")
    if not isinstance((name := data.get('name')), str):
        errors.append(F"name should be type string got {type(name)}")
    if not isinstance((phone_no := data.get('phone_no')), str):
        errors.append(F"phone_no should be type string got {type(phone_no)}")
    else:
        phone_no_pattern = r'\+\d{12}'
        match = re.match(
            phone_no_pattern,
            phone_no,
        )
        if not match:
            errors.append(F"phone_no did not match the RegEx {phone_no_pattern}")
    if len(errors) != 0:
        raise InvalidDataError(
            ' | '.join(errors)
        )


class ClientError(Exception):
    """raised when unable to start database session"""


database_failed_lately = True
database_current_session_id = None


def start_database_session() -> str:
    """rickety function, fails alternatingly. Either returns a
    session id or raises a ClientError"""
    global database_failed_lately
    if database_failed_lately:
        global database_current_session_id
        database_current_session_id = str(uuid4())
        database_failed_lately = False
        return database_current_session_id
    else:
        database_failed_lately = True
        raise ClientError('Session unable to be established')


class DatabaseError(Exception):
    """raised when database operation fails"""


database_records = {}


def put_data(session: str, data: dict):
    """raises DatabaseError if id is already present in database or
    session not valid"""
    if database_current_session_id != session:
        raise DatabaseError(
            "Session mismatch, open new session first"
        )
    id = data.get('id')
    if database_records.get(id):
        raise DatabaseError(
            F"record with id '{id}' already exists in database"
        )
    else:
        database_records[id] = data
    return {'status': 200}


if __name__ == "__main__":

    id = str(uuid4())
    data = {'id': id, 'name': 'max', 'phone_no': '+447709852336'}
    validate_data(data)
    session_id = start_database_session()
    put_data(data)
    put_data(data)
