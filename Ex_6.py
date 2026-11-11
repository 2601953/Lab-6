'''
In your function, you are reinitializing the variable total in each iteration.
Instead you should assign in the loop, and initialize before it.
'''

def total_sum(lst):
    total = 0
    for x in lst:
        total += x
    return total

print(total_sum([1, 2, 3, 4, 5])) # The output should be 15

