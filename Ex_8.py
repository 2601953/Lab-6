'''
 In your code, you return none if the current number is not even, as such
 You either find it first try, or return none after the first test.
 Return none should be outside of your loop.
'''

def find_first_even_number(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number
    return None

print(find_first_even_number([1, 3, 5, 7, 8, 9])) # The output should be 8