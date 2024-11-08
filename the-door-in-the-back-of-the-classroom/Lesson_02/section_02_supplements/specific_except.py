from number_gate import positive_number_gate


if __name__ == "__main__":
    try:
        positive_number_gate("I ain't no number!")
    except TypeError:
        print("Whoops! That wasn't a number")
