num1 = 11
num2 = num1

print("Before updating the num1 value")
print("num1 is : ", num1)
print("num2 is : ", num2)

print("ID of num1: ", id(num1))
print("ID of num2: ", id(num2))

num1 = 22

print("After updating the num1 value")
print("num1 is : ", num1)
print("num2 is : ", num2)

print("ID of num1: ", id(num1))
print("ID of num2: ", id(num2))