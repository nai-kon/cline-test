def fizzbuzz(number):
    """Return 'Fizz', 'Buzz', 'FizzBuzz', or the number as a string based on FizzBuzz rules."""
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)