class FakeValue:
    def __init__(self):
        self.call_count = 0

    def callable(self, value_as_abc):
        if value_as_abc:
            value = "ABC"
        else:
            value = "123"

        self.call_count += 1
        return value, self.call_count

    def caller(self):
        value_as_abc = True

        while self.call_count < 3:
            value, call_count = self.callable(value_as_abc)
            print("Value:", value)
            print("Call count:", call_count)

        value_as_abc = False
        value, call_count = self.callable(value_as_abc)
        print("Value:", value)
        print("Call count:", call_count)


fake_value = FakeValue()
fake_value.caller()
