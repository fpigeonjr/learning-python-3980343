# count the number of even or odd numbers in a list
# params which = "even" or "odd" and numbers = number[]

numbers = [2, 5, 20, 30, 55]

def count_number(which, numbers):
    which = which.lower()
    count = 0

    if which == "even":
        for num in numbers:
           if num % 2 == 0:
              count += 1
    elif which == 'odd':
        for num in numbers:
           if num % 2 != 0:
              count += 1
    else:
        count = -1

    return count

print(count_number('even', numbers)) # 3
print(count_number('odd', numbers)) # 2
print(count_number('bla', numbers)) # -1


# better solution
#
def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

def count_number2(which, numbers):
    which = which.lower()
    count = 0

    if which != 'odd' and  which != 'even':
        return -1

    for num in numbers:
        if which == "even" and isEven(num):
            count += 1
        elif which == "odd" and not isEven(num):
            count += 1
    return count

print(count_number2('even', numbers)) # 3
print(count_number2('odd', numbers)) # 2
print(count_number2('bla', numbers)) # -1
