#creates a list of numbers from 1 to 15
numbersList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#iterates through the list
for number in numbersList:
    #If the number is even, print number is even
    if number % 2 == 0:
        print(str(number) +  " is even")
        #else print number is odd
    else:
        print(str(number) + " is odd")