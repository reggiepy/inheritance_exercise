# This is a sample Python script.

class BaseClass:
    num_base_calls = 0

    def call_me(self):
        print(f"Calling method on {BaseClass.__name__}")
        self.num_base_calls += 1


class LeftBaseClass(BaseClass):
    num_base_calls = 0

    def call_me(self):
        BaseClass.call_me(self)
        print(f"Calling method on {LeftBaseClass.__name__}")
        self.num_base_calls += 1


class RightBaseClass(BaseClass):
    num_base_calls = 0

    def call_me(self):
        BaseClass.call_me(self)
        print(f"Calling method on {RightBaseClass.__name__}")
        self.num_base_calls += 1


class SubClass(LeftBaseClass, RightBaseClass):
    num_base_calls = 0

    def call_me(self):
        LeftBaseClass.call_me(self)
        RightBaseClass.call_me(self)
        print(f"Calling method on {SubClass.__name__}")
        self.num_base_calls += 1


if __name__ == '__main__':
    s = SubClass()
    s.call_me()
    print(SubClass.mro())
    print(s.num_base_calls)
