from number_gate import positive_number_gate


if __name__ == "__main__":
    # open file
    file_stream = open('test.txt', mode='w')
    try:
        # attempt writing into file while doing dodgy stuff that
        # might raise an error
        file_stream.write('hello\n')
        file_stream.write('trying to split self\n')
        positive_number_gate("I ain't no number!")
        file_stream.write('successfully split self\n')
    except Exception:
        # upon catching error, gracefully flush and
        # close the file_stream
        file_stream.flush()
        file_stream.close()
        # then re-raise the error
        raise
