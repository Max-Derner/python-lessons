from dodgy_module import dodgy_function


for item in ['sea', 'cat', 1, {'tres': 'bien'}]:
    try:
        print(
            dodgy_function(item)
        )
    except Exception as e:
        print(F"EXCEPTION using item {repr(item)}: {repr(e)}")
