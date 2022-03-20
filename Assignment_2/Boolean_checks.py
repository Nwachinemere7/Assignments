# ## 5. 
# #Variables x and y refer to Boolean values.
# #a. Write an expression that produces True if both variables are True.

# #Solution:
and_function = True and True
print(and_function)

x = 3 
y = 5

testValue = (x < 5 and y > x)
print(testValue)

# #b. Write an expression that produces True if at least one of the variables is True.

# #Solution:
or_function = True or False
print(or_function)

x = 3 
y = 5

testValue2 = (x == 5 or y > 3)
print(testValue2)

# #c. write an expression that inverses the result of 5a above.

# #Solution:
and_not_function = True and  not True
print(and_not_function)

x = 3 
y = 5

testValue3 = (x < 5 and not y > x)
print(testValue3)