def greaterThan(x, y):
    #if x is greater than y return true
    if x > y:
        return True
    else:
        #Should return false if x is not greater than y
        return False
#Test cases
a = 2
b = 3
result = greaterThan(a, b)
print(result)
a = 10
b = 6
result = greaterThan(a, b)
print(result)