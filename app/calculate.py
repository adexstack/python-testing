class Calculate(object):
    def add(self, x, y):
        """
        Takes two integers and adds them together to produce the result.
        >>> c.add(1, 1)
        3

        >>> c.add(25, 125)
        150

        >>> c.add(1.0, 1.0)
        Traceback (most recent call last):
         ...
        TypeError: Invalid type: <type 'float'> and <type 'float'>
        """
        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid Type: {} and {}".format(type(x), type(y)))


if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'c': Calculate()})
    # calc = Calculate()
    # result = calc.add(2, 'Dan')
    # print(result)
