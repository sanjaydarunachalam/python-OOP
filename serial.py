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
    def __init__(self, start =0):
        """ makes new generator, with inital value of start"""
        self.start = self.next = start

    def __repr__(self):
        """user friendly representation of values within class"""

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """returns next number"""
        self.next +=1
        return self.next -1

    def reset(self):
        """reset number back to starting value"""
        self.next =self.start
        



