# ## 8.

# # Write a program that reads a sound level in decibels from the user. 
# # If the user enters a decibel level that matches one of the noises in the table then your program should display a message containing only that noise.
# # If the user enters a number of decibels between the noises listed then your program should display a message
# # indicating which noises the value is between. 
# # Ensure that your program also generates reasonable output for a value smaller than the quietest noise in the table, 
# # and for a value larger than the loudest noise in the table.

# #Solution:

# #Using information collected from American Academy of Audiology.

levels_of_noise = {(float('-inf'), 29): "Faint Noise", 
              (30, 49): "Soft Noise",
              (50, 69): "Moderate Noise",
              (70, 89): "Loud Noise",
              (90, 119): "Very Loud Noise",
              (120, 129): "Uncomfortable Noise",
              (130, float('inf')): "Painful and Dangerous Noise"
}

noise_value = (input("Please, input the level of noise value in decibels here: "))

#error check, to ensure only numeric values are inputs.
if noise_value.isnumeric():

    for (x, y) in levels_of_noise:
        if (x <= float(noise_value) and y >= float(noise_value)): #condition selecting the range of noise level.
            noise = levels_of_noise[(x, y)]
            print("The noise level is: {}".format(noise))
else:
    print("Otondo, only numeric values are allowed. Try again!!")