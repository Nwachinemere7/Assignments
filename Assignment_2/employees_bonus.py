# ## 9. 

# # A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# # Write a code that asks the user to input their salary and years of service and then prints the net bonus amount.
# # Use string format method

#Solution:

#collecting information of the workers.
title = str(input("Please enter your title (Mr, Mrs, Ms, Miss, Chief): ")).capitalize()
first_name = str(input("What is your First name? : ")).capitalize()
surname = str(input("What is your Surname? : ")).capitalize()
initial_salary = float(input("What is your current salary? : "))
service_yrs = float(input("How long have you served this company? : "))

#calculating their bomus.
bonus_percent = 0.05

def bonus(bonus_percent, initial_salary):
    if service_yrs >= 5:
        return (bonus_percent * initial_salary) + initial_salary
    else:
        return initial_salary

new_salary = bonus(bonus_percent, initial_salary)

print("Hello {}. {} {}. Your salary for the month {}.\n Thank you your service." .format(title, first_name, surname, new_salary))

