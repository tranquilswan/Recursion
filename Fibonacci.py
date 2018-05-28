#find the fibonacci sequence of a given number
#the problem can be reduced down to calculating (num - 2) + (num - 1)
def calcFib(num):
    if(num == 0):
        return 0
    elif(num == 1):
        return 1
    else:
        return calcFib(num - 1) + calcFib(num - 2)


num = int(input("enter a number: "))
print("the fib sequence for ",num,":",calcFib(num))
#this is a good demo of how to use recursion to calulate fin sequences, but its hella inefficient
#because it repeates itself too much


# implementation using loops

num = int(input("enter a number: "))
f0 = 0
f1 = 1
fibNum = 0
for i in range(1,num,1):
    fibNum = f0 + f1
    f0 = f1
    f1 = fibNum

print("fib sequence of",num,"using loops is:",fibNum)

'''
if we consider the java rendition of the above implementation (For readability):
num = 4                     |Pass 1     |Pass 2     |Pass 3     |Pass 4     |Pass 5
for (i = 1; i<num; i++){    |i=1        |i=2        |i=3        |i=4        |i=5
    fibNum = f0 + f1        |fibNum=1   |fibNum=2   |fibNum=3   |fibNum=5   |EXIT
    f0 = f1                 | f0 = 1    | f0 = 1    | f0 = 2    | f0 = 3    |
    f1 = fibNum             | f1 = 1    | f1 = 2    | f1 = 3    | f1 = 5    |
}                           | i = 2     | i = 3     | i = 4     | i = 5     |

so in a for-loop implementation it makes 4 passes and get to the right answer,
In a recursive implementation it takes 17 steps (according to literature), also
have to remember that it performs multiple duplicate recursive calls. Waste of computation power
and for larger numbers your system will encounter problems 

'''