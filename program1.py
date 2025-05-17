# question1: Write a Python program that takes a number as user input and checks whether it is even or odd.
n=int(input("enter the number"))
p=False
for i in range(2,n//2+1):
    if n%i == 0:
        p=True
if p:
    print("even")
else:
    print("odd")
    
    
# question2:  Write a Python program that takes three numbers as user input and finds the largest among them
a=input("enter first number:  ")
b=input("enter second number: ")
c=input("enter thired number: ")
largest=0
large=max(a,b,c)
print(large)
# or
if a>b and a>c:
    largest=a
elif b>c :
    largest=b
else:
    largest=c





# question3: Write a Python program that takes a number as input and checks if it is positive, negative, or zero using if-elif-else.
n=int(input("enter the number: "))
if n>0:
    print("positive")
elif n<0:
    print("negative")
else:
    print("zero")
    
    


# question4: What is the difference between a for loop and a while loop? Provide examples of both.
for i in range(10):
    print(i)
    # For loop executes usually starts with 0 till the range given.

i=10
while i>0:
    print(i)
    i-=1
    # while will execute till the condition is true
    

    
# question5:  What is the difference between if and nested if? Provide examples.
# if condition comes with one condition and one ifnot(else) statement. it can be executed without else condition also.
a,b=0,1
if b>a:
    print("b is largest")
else:
    print("a is largest")
# nested if conditions are multiple if conditions, one inside the other.
c=3
if b>a:
    if b>c:
        print("b is greater")
elif a>b:
    if a>c:
        print("a is greater")
else:
    print("c is greater")




# question6: What is the difference between if-else and elif? Provide examples.
# if-else runs like a branch. where if the condition is true run the code present or it will run the else code.
if b>a:
    print("b is largest")
else:
    print("a is largest")
# elif is else-if in python, used when we want to put another condition to check if not the first condition, it can be true for another condition and then else conditions also comes in the end.
if b>a:
    if b>c:
        print("b is greater")
elif a>b:
    if a>c:
        print("a is greater")
else:
    print("c is greater")
    
    
    
# question7: Write a program that prints all prime numbers between 1 and a user-entered number.
def prime(num):
    p=True
    for i in range(2,(num//2)+1):
        if num%i==0:
            p=False
            return p
    return p
def prime_numbers(n):
    l=[]
    for i in range(1,n):
        if prime(i):
            l.append(i)
    return l

n=int(input("enter the limit to prime numbers: "))
print(prime_numbers(n))



# question8: Write a Python program that takes an integer n from the user and prints the Fibonacci series up to n terms.
def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
n = int(input("Enter the number of terms in the Fibonacci series: "))
for i in range(n):
    print(fibonacci(i), end=" ")

      
# question9: Write a function that takes a string input from the user and returns the reversed string without using [::-1] or reversed().
def rev(s):
    return s[::-1]
s=input("enter the string: ")
print(rev(s))
# or
def string_rev(s):
    return reversed(s)
s1=input("enter the string: ")
print(rev(s1))



#question10: Write a Python function that takes a sentence as input and counts the number of vowels in it.
def count_vowels(sentence: str) -> int:
    vowels = "aeiouAEIOU"  
    count = 0  
    
    for char in sentence:
        if char in vowels:
            count += 1  
    
    return count  

sentence = input("Enter a sentence: ")
print(count_vowels(sentence))



# question11: Write a Python program that takes a list of numbers as input from the user and removes duplicates without using set().
l=list(input("enter the list: ").split(" "))
l=list(set(l))
print(l)



# question12: Write a Python program that takes a sentence as input and counts the occurrences of each word using a dictionary.
def count_word_occurrences(sentence: str) -> dict:
    sentence = sentence.lower()
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1  
        else:
            word_count[word] = 1  
    return word_count

sentence = input("Enter a sentence: ")
word_count = count_word_occurrences(sentence)
print("Word occurrences:")
for word, count in word_count.items():
    print(f"'{word}': {count}")
    
    
    
#question13: Write a program that takes a tuple of numbers from user input and finds the second-largest element without converting it into a list.
t=eval(input("enter the tuple members: (as ""(1,2,3)"")"))
t1=sorted(t)
print(t1[-2])


#question14:  Write a program that takes a tuple of numbers from user input and returns a new tuple containing only the even numbers.
t=eval(input("enter the tuple members: (as ""(1,2,3)"")"))
t1=()
for i in t:
    if i%2==0:
        t1 += (i,)
        
print(list(set(t1)))


#question15: Write a Python program that accepts a list of numbers from the user, sorts them in ascending order, and prints both the original and sorted list.
l=list(input("enter the list: ").split())
print(l)
print(sorted(l))


