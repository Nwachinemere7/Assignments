# ## 7.

# # Write a program that reads the name of a month from the user as a string. Then your program should display the number of days in that month. Display “28 or 29 days” for February so that leap years are addressed.

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

user_month_input = str(input("Kindly input the name of the month: ")).capitalize()
if user_month_input in months:
      print("Lets check the number of days in the month!")
      if user_month_input in ("April", "June", "September", "November" ):
            print("This month has 30 days")
      elif user_month_input in ("January", "March", "May", "July", "August", "October", "December"):
            print("This month has 31 days")
      else:
            print("This month can be a leap month. It can have 28 or 29 days.")
else:
      print("This is a invalid input. Try again!!")

