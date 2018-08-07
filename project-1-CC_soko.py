#Challenge 1: Largest Palindrome
"A palindromic number reads the same both ways. For example, 1234321 is a palindrome. The largest palindrome made from the product of two two-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two three-digit numbers. Afterward, write a brief explanation walking through your code's logic in markdown."

Palindrome = 0
for x in range(100, 1000):
    for y in range(100, 1000):
        z = x * y
        if str(z) == ''.join(reversed(str(z))):
            Palindrome = max(Palindrome, z)
print(Palindrome)
# This is done on a for loop to make sure it runs all the combinations
# Ranges for both x and y are from 100 to, but not inlucding, 1000
# z = all the cross products of the combinations
# 'str' added to ensure results are converted to characters.
#'Join  + reversed' are there to join the products in reverse order to check for palindromic characters

#Challenge 2: Summation of Primes
"The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below 2,000. Afterward, write a brief explanation walking through your code's logic in markdown."

def Prime(n):
    if n < 2: return "Unit: neither prime nor composite"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
sum = 0
for i in range(2, 2001):
    if Prime(i):
        sum += i
print (sum)
#Any number below 2 is called a unit, which is neither prime or a composite
#function will return false if number is neither prime or composite otherwise, a True will be returned for prime numbres
# +1 because python goes up to but not including the last value
#The nested for loop is there to do the calculations
#For large numbers, the square root is used because they keep repeating themselves, thus no need to check for primeness.
#The square root should also improve the performance of the computer.
# I chose not to import the math function (squar root) because this is the only place that I need that special math function
#The square root checks for primeness, numbers repeat themselves after a multiple of the square root of that number
#The % sign is used to test for divisors. Any number resulting in zero, is not prime


#Challenge 3: Multiples of 3 and 5¶
"If we list all of the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 and 5 below 1,000. Afterward, write a brief explanation walking through your code's logic in markdown."
total = 0
for i in range(1000):
#In this function, we're using the mod function to check for all natural numbers--remainder of 3 and 5
#At the top, the 'total' accumulate all the sum from the operations.
#Added the 'i' to catch the sum of all the numbers
    if (i%3 == 0 or i%5 == 0):
        total = total+i
print (total)

"Alternatively, I tried solving the problem using the 'generator' of pyton3 to solve this problem:"
#print(sum(i for i in range (1, 1000) if i % 3 == 0 or i % 5 == 0))

#Challenge 4: String Compressor¶
"Implement a method to perform basic string compression using the counts of repeated characters. (This is called run-length encoding.) For example, the string "'aabcccccaaa'" would become a2b1c5a3. If the “compressed” string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a–z). Specify whether your solution is case sensitive or case insensitive and what you would need to change to make it the other. Afterward, write a brief explanation walking through your code's logic in markdown."

input1 = 'aabcccccaaa'
input2 = 'aaaaaabbbbccccccccaaaaaaaaabbbbbbbbb'
def stringcompressor(input):
    comp_str = ""
    count = 1
    for i in range(len(input)-1):
        if input [i]== input [i + 1]:
            #check to see if the character is equal to the last one, if true, you increment the count.
            count += 1
        else:
            comp_str += input [i] + str (count)
            count = 1
            #This checks and adds to the next set of same characters
    comp_str += input[i] + str(count)
    #This is added again outside the 'if statement', but in the 'for loop' to ensure that it repeats the loop
    if len(comp_str) >= len (input):
    #This is to figure out if the output is greater than the input
        return input
    else:
        return comp_str
print (stringcompressor(input1))
print (stringcompressor(input2))

#BONUS Challenge: FizzBuzz
"Write a program that prints all of the numbers from 1 to 100. For multiples of 3, instead of the number, print Fizz; for multiples of 5, print Buzz. For numbers that are multiples of both 3 and 5, print FizzBuzz."

for i in range (1, 101):
    if (i % 5 == 0 and i % 3 == 0):
        print ('FizzBuzz')
    elif i % 3 == 0:
        print ('Fizz')
    elif i % 5 == 0:
        print ('Buzz')
    else:
        print (i)
#This problem is similar to challenge question 3.
#It loops through the range of numbers from 1 up to, but not including 101
#Like in Challenge 3, i'm using the mod function to checks for natural number looking for 3 or 5
#I'm testing for 4 conditions: 3&5, 3, 5 and everything else.
