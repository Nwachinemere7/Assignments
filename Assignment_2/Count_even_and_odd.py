# ## 13.

# Write a program to count the number of even and odd numbers between 10 and 40
#Solution:
count_even = 0
count_odd = 0
for num in range(10, 40):
      if num % 2 == 0:
            count_even += 1
      else:
            count_odd += 1
print(f'There are {count_even} even numbers from the range')
print(f'There are {count_odd} odd numbers fro the range')