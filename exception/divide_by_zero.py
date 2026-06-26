class DivisionByZeroError(Exception):
    # Custom exception is raised when attempting to divide by zero.
    # don't modify this custom exception class
    pass


# TODO : raise DivisionByZeroError if divisor is zero, return result otherwise
def divide_numbers(dividend, divisor):
    # Complete the code
    if divisor == 0:
        raise DivisionByZeroError('Cannot divide by zero')
    else:
        return dividend/divisor

