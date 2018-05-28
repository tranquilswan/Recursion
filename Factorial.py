#calculating factorials and similar probs using recursion

def calcFac(num):
    if(num == 1):
        return 1
    else:
        return num * calcFac(num - 1)

print("factorial of 5:",calcFac(5))
'''
When called, this method should add all the numbers below the given number togeather
the functions makes recursive calls to itself
    subtracts one from the provided number, calls itself, checks if the number is down to one,
    if not, repeat. if yes, return one,
'''

def sumMethod(number):
    if(number == 1):
        return 1
    else:
        return number + sumMethod(number - 1)

'''
For 5, it'll go like this:
    #5 + s(5-1=4)
        #4 + s(3)
            #3 + s(2)
                #2 + s(1)
                    #1
'''
# print("sum is",sumMethod(5))


#This program should output all the times the division by ten happens
#should just end, there is no else.
def modMethod(number):
    if(number > 0):
        print(number % 10)
        modMethod(number / 10)

# print("modMethod output:",modMethod(1234567))

'''
what happened? well, if i run with the term command, the output is different from the play button.
with terminal command, the number kept dividing, it had turned to the XXeYY notation.
with the play button it stopped at 10.
'''