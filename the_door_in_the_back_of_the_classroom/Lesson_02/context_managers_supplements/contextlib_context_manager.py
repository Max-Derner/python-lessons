from contextlib import contextmanager


@contextmanager
def my_context_manager():
    # enter style code
    try:
        yield  # some resource
    # optional except here for suppressing exceptions
    finally:
        # some code to release resource
        pass


if __name__ == "__main__":
    with my_context_manager():
        pass
