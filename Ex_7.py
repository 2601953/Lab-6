'''
In your loop, you are incrementig both n and i, so i never catches up to n
Therefore, it becomes infinite.
If you want to also include 10, it should be <=10
Alternatively, you could have the print after the incremement, and start at -1 
but thats weird
'''

n = 10
i = 0
while i <= n:
    print(i)
    i += 1
