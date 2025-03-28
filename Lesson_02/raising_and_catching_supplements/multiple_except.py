from number_gate import positive_number_gate


if __name__ == "__main__":
    for item in [-1, 'two', 1]:
        print(F"\nUsing item: {repr(item)}")
        try:
            positive_number_gate(item)
            print("Hey! That was a good number")
        except (TypeError, ValueError):
            print("Ooops! Something went wrong there!")
