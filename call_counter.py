call_count = 0

def callable(value_as_abc):
    global call_count
    if value_as_abc:
        value = "ABC"
    else:
        value = "123"

    call_count += 1
    return value, call_count

def caller():
    global call_count
    value_as_abc = True

    while call_count < 3:
        value, call_count = callable(value_as_abc)
        print("Value:", value)
        print("Call count:", call_count)

    value_as_abc = False
    value, call_count = callable(value_as_abc)
    print("Value:", value)
    print("Call count:", call_count)

caller()
