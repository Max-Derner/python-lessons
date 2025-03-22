from dodgy_module import dodgy_function


for item in ['sea', 'cat', 1, {'tres': 'bien'}, {'s', 'e', 't'}]:
    try:
        print(
            dodgy_function(item)
        )
    except (TypeError, KeyError) as e:
        print(F"EXCEPTION using item {repr(item)}: {repr(e)}")
    except Exception as e:
        print(F"UNEXPECTED EXCEPTION: {repr(e)}")
