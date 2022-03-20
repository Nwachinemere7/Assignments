# ## 6.
# #Write a program that begins by reading the denomination of Naira banknote from the user. 
# # Then your program should display the name of the individual that appears on the banknote of the entered amount. An appropriate error message should be displayed if no such note exists.
# # tip: your code will be tested with all naira notes, so make sure you put that into consideration

# #Solution:

naira_denominations = [1000, 500, 200, 100, 50, 20, 10, 5]

all_naira_notes = {1000: "Alhaji Aliyu Mai-Bornu and Dr Clement Isong", 500: "Dr Nnamdi Azikiwe", 200: "Ahmadu Ibrahim Bello", 100: "Chief Obafemi Awolowo", 50: "The People o fNigeria", 20: "General Murtala Mohammed", 10: "Mazi Alvan Ikoku", 5: "Sir Abubakar Tafawa Balewa"}

user_input = int(input("Enter the value of the denomination: "))

if user_input in naira_denominations:
      print("Welcome")
      print(f'The the value input is a {user_input} naira note.')

      for x in all_naira_notes.keys():
            if user_input == x:

                  print("The individual(s) on the denomination is(are): {}".format(all_naira_notes.get(x)))

else:
      print("This is not a correct input. Try again!!")
