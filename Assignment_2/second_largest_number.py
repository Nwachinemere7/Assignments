# ## 11.

# Write a program that accepts three numbers from the user and displays the second largest number.

#Solution:

user_input = (input("Enter three digit number: "))

num_list = [ ]
if len(user_input) == 3: #checking the user not to input more than 3 digits numbers
    num = str(user_input)
    #iterate over the converted string(num) and append it to the list variable.
    for i in num:
        num_list.append(i)
        #sort the list in descending order using the sort method.
    num_list.sort()
    print(f'The Second largest number is: {num_list[-2]}')
else:
    print("Wrong input of number of digits. Kindly insert a three digit value.")
