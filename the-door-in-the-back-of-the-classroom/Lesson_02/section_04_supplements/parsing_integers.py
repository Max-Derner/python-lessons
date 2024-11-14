

def parse_integer(txt: str) -> int | None:
    """Parses integers from input `txt`,
    logs to a file called `logs.txt` which will appear in the same
    directory you are running the code from"""
    with open("logs.txt", mode='a') as logs:
        logs.write("===============================\n")
        logs.write(F"Beginning to parse '{txt}'\n")
        try:
            num = int(txt)
        except ValueError:
            logs.write("FAILED\n")
        else:
            logs.write("SUCCESS\n")
            return num
        finally:
            logs.write(F"Finished parse of '{txt}'\n")


if __name__ == "__main__":
    samples = [
        "1",
        "1.1",
        "I",
        "2",
    ]
    outputs = []
    for item in samples:
        returned = parse_integer(item)
        if returned is not None:
            outputs.append(returned)
    print(F"Tried: {len(samples)} inputs")
    print(F"{len(outputs)} successful")
