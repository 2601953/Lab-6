# Error 
# You are comparing each element with the element at index a, rather than 
# The value of variable a.
# Further more your range should start at 0, not 1.
# Finally, you should assign lst[x] to a, not x.

def minimum(lst):
    a = 0
    for x in range(1, len(lst)):
        if lst[x] < lst[a]:
            a = x
    return a

def corrected_minimum(lst):
    a = 2147483647 # Pretend its 32 bit
    for x in range(0, len(lst)):
        if lst[x] < a:
            a = lst[x]
    return a

print(minimum([4, 2, 7, 3])) # The output should be 2
print(corrected_minimum([4, 2, 7, 3])) # The output is 2