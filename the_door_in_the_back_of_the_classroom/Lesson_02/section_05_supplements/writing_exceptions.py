from traceback import format_exception

EXCEPTION_FILE = 'exceptions.txt'


def exception_writer(e: Exception):
    with open(EXCEPTION_FILE, mode='a') as f:
        f.write(
            '\n'.join(format_exception(e))
        )


if __name__ == "__main__":
    try:
        'me'/2
    except Exception as e:
        exception_writer(e)
        raise
