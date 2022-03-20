# ## 10.

# Write a program to display all prime numbers between 10 to 80.

#Solution:

lower = 10
upper = 80

#iterating the range of values
for number in range(lower, upper):
    if number >= 1:
          #diving every number in the range to check if it divisible by any other number but itself and 1
        for i in range(2,number):
            if (number%i) == 0:
                break  #breaks when if finds the number can be divisible aby another num
        else:
            print(number)