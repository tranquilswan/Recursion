#check if a given word is a palindrome

def checkPalin(word):
    if(len(word) <= 1):
        print("YES SEY")
        return True
    elif(word[0] != word[len(word)-1]):
        print("NO ON")
        return False
    else:
        return checkPalin(word[1:-1])



word = input("enter a word:")
checkPalin(word)