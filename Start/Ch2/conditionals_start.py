x, y = 10, 100 # can declare multiple variables on one line

# conditional flow uses if, elif, else
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x is equal to y')

# conditional statements let you use "a if C else b"
# ternary is js
result = "x is less than y" if (x < y) else "x is geater or equal to y"
print(result)
