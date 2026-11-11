numbers = [10, 20, 30, 40]

try:
    index = int(input("Enter an index number: "))
    divisor = int(input("Enter a divisor: "))


    final = numbers[index] / divisor
    print("The result is: ", final)
except IndexError:
    print("Error: Index out of range.")
except ZeroDivisionError:
    print("Error: Division by zero.")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")
except Exception as e:
    print("you somehow broke everything: ", str(e))
