"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Create serial number generater starting at the number you provide"""
        self.start = start
        self.next = start

    def __repr_(self):
        """returns rep of function"""
        return f"<SerialGenerator(start={self.start})"

    def generate(self):
        """Returns next sequential number and incruments the starting number"""
        temp = self.next
        self.next += 1
        return temp

    def reset(self):
        """resets the next sequential number back to original starting number"""
        self.next = self.start
