from math import *

print(-2)
print(44)
print(2+44)
print(-2+44)                                         #by adding a minus number to a natural number the answer will resemble a subtraction
print(2*44)
print(7*5+15)                                        #multiplying using * will be prioritesed over addition
print(7*(5+15))                                      #using parentheses prioritises the specifies the order of operations
print (10 % 3)                                       #the Modulus operator "%" divides a value and retrieves the remainder of the operation
print (20 % 4)                                       #the modulus operator divides the first number by the second and retrieves the remainder
print (40 * (17%6))                                  #by prioritising the modulus operation with brackets we get the answer "5" and this is used to multiply 40

my_number = 10
print(my_number + my_number)                         #as the datatype is not specified in this line of code the computer automatically assumes it is an integer value from the line above
print(str(my_number)+str((my_number)))               #in this line I assign the datatype "string" so it is not recognized as a whole number, much rather a word thus making a mathematical equation impossible and duplicating the value
print(2 * (str(my_number)))                          #i have repeated this process but shortened the code by duplicating with an integer
my_number2 = -35
print(my_number2)
print(abs(my_number2))                               #"abs" function means absolute value and will retrieve the non negative value of the number
print(pow(3,2))                                #"pow" function will take the first given number the the power of the second number
print(3 * 3)
print(pow(4,4))
print(4 * 4 * 4 * 4)
print(max(1,92))                                     #"max" function will retrieve the highest of the 2 numbers that are given
print(min(41,70))                                    #"min" function will retrieve the lowest of the 2 numbers that are given
print(round(44.5))                                   #"round" function rounds the decimal number to the closest integer
print(round(44.6))
print(str(my_number)+ " " +str((my_number)))

#These functions are given to use via "from math import *" module

print(floor(3.7))                                    #"floor" retrieves the lowest number
print(ceil(3.7))                                     #"ceil" retrieves the highest number
print(sqrt(81))                                      #"sqrt" retrieves the square root of a number