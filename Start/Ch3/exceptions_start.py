# Errors can happen in programs, and we need a clean way to handle them
# This code will cause an error because you can't divide by zero:
# x = 10 / 0
# Exceptions provide a way of catching errors and then handling them in
# a separate section of the code to group them together
try:
    x = 10 / 0
except:
    print('error')

# You can also catch specific exceptions
try:
    answer = input("What should I divide 10 by: ")
    num = int(answer)
    print(f"10 divided by {num} is {10 / num}")
except ZeroDivisionError as e:
    print("You can't divide by zero")
except ValueError as e:
    print("You didn't provide a valid number")
    print(e)
finally:
    print("Finally always runs")
