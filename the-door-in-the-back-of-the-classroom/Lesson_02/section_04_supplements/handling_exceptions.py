from writing_exceptions import exception_writer


def operate(a: int, b: int) -> float:
    return a / b


if __name__ == "__main__":
    try:
        numerator = int(input("Input a numerator! "))
        denominator = int(input("Input a denominator! "))
        result = operate(numerator, denominator)
    except Exception as e:
        exception_writer(e)
        print(F"Whoops! Thrown a {repr(e)}")
    else:
        print("All ok!")
        print(F"Your result is: {result}")
    finally:
        print("All done!")
        exit(0)
