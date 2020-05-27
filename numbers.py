import math

pi = math.pi
print('{:.2f}'.format(pi)) #formating decimal numbers by the right way
print(f'{pi:.4f}')  #formating decimal numbers by a simple way

num1 = input("Please enter the first number") #this way, the value will be gotten as default(as a string)
num2 = input("Please enter the second number") #this way, the value will be gotten as default(as a string)
print(num1 + num2) #result:concat strs
num_1 = float(input("Please enter the first number")) #here there is a conversion to float been made
num_2 = float(input("Please enter the first number")) #here there is a conversion to float been made
print(num1 + num2)#result: concat strs too
print(float(num1) + float(num2)) #result: sum of the two numbers
