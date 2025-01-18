from datetime import datetime
from traceback import format_exception


nums_to_sum = [1, 10, 100, "1", 42, 999]

with open("logs.txt", mode='w') as logs:  # get our log file going
    try:
        # do a bunch of stuff
        logs.write(F"Starting work at {datetime.now()}\n")
        a = 0
        nums_summed = 0
        for num in nums_to_sum:
            logs.write(F"Adding {num=}, {nums_summed=}\n")
            a += num
            nums_summed += 1
        logs.write("Finished work successfully\n")
    except Exception as e:
        # if anything goes wrong, write that to file
        logs.write(F"Failed work after summing {nums_summed} nums\n")
        logs.write("EXCEPTION:\n")
        logs.write(format_exception(e))
