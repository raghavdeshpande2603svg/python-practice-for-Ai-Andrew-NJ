# #here we use def keyword to define the function in the python and we use the return keyword to return value form the function.
# def evenOdd(num):
#     if num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")

# print(evenOdd(5))
# print(evenOdd(26))

# def student(fname, lname):
#     print(fname, lname)

# student(fname='Geeks', lname='Practice')
# student(lname='Practice', fname='Geeks') ##used to print the first name and last name using the keywords at the starting of the argumments of the program.


# ##pass by refrence and pass by value in python 
# def myFun(x):
#     x[0] = 20 ## pass by refrence as the reference of the index is give here form the array

# b = [10, 11, 12, 13]
# myFun(b)
# print(b)

# def myFun2(x):
#     x = 20 ##pass by value as the value of the variable is given here and not the reference of the variable.

# a = 10
# myFun2(a)
# print(a)

# items = [3, 4, 1, 2, 5]
# items.sort() ##sort function is used to sort the given list in ascending order.
# print(items)


import numpy as np
import matplotlib.pyplot as plt
X = np.array([500, 750, 1000, 1250, 1500, 1750, 2000, 2250])  ##house size
Y = np.array([30, 42, 55, 67, 80, 92, 105, 118]) ##house prize


print("Area: ", X)
print("Price: ", Y)

m = 0.07
c = 0


prediction = m*X + c
error = Y - prediction
print(prediction)
print(error)


plt.scatter(X, Y)
plt.plot(X, prediction)

plt.xlabel("House Area")
plt.ylabel("House price")
plt.title("House Price Prediction model")


plt.show()
