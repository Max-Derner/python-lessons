from datetime import datetime


def parse_integer(txt: str) -> int | None:
    """Parses integers from input `txt`,
    logs to a file called `logs.txt` which will appear in the same
    directory you are running the code from"""
    with open("logs.txt", mode='a') as logs:
        logs.write("===============================\n")
        logs.write(F"Beginning to parse '{txt}'\n")
        try:
            # smallest part in try block
            num = int(txt)
        # ValueError is all that should be raised when
        #  failing a type cast
        except ValueError:
            # log failure when it fails
            logs.write("FAILED\n")
        else:
            # log success when no ValueError thrown
            logs.write("SUCCESS\n")
            # return your value over here in the success block
            return num
        finally:
            # declare finished, this will actually intercept the return
            #  statement above
            logs.write(F"Finished parse of '{txt}'\n")


if __name__ == "__main__":
    print("Logs will go to 'logs.txt'")
    with open("logs.txt", mode='w') as logs:
        logs.write(F"Starting program at {datetime.now()}\n")
    for item in ['1', '2', '3', 'four']:
        print(F"Trying to parse {repr(item)}")
        returned = parse_integer(item)
        print(F"Got {repr(returned)}")
