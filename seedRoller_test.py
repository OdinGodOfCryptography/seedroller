#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import numerical and plotting library
import numpy as np
import matplotlib.pyplot as plt

# https://www.random.org/analysis/

# Here we roll the dice using the numpy random functions
# seven d6
no_rolls = 10000000
rolls = np.random.randint(1,7, size=(no_rolls,7))

rolled_numerals = np.zeros((no_rolls,4), dtype=int)
frequency_counter_d6 = np.zeros(3000, dtype=int)

for i in range(0, no_rolls):
    # For each roll of seven dice, we now designate the different dice
    # to the thousands, hundreds, tens and ones counters in order to
    # find a given number from 0 to 2999
    
    # thousands, 10^3
    thousands = np.int(np.ceil( rolls[i,0] /2 ) ) - 1
    rolled_numerals[i,0] = thousands
              
    # hundreds, 10^2
    if rolls[i,1] <=3:
        while rolls[i,2] == 6:
            rolls[i,2] = np.random.randint(1,7)
        if rolls[i,2] == 5:
            hundreds = 0
        else:
            hundreds=rolls[i,2]
    else:
        while rolls[i,2] == 6:
            rolls[i,2] = np.random.randint(1,7)
        hundreds=rolls[i,2] + 4
    rolled_numerals[i,1] = hundreds

    # tens, 10^1
    if rolls[i,3] <=3:
        while rolls[i,4] == 6:
            rolls[i,4] = np.random.randint(1,7)
        if rolls[i,4] == 5:
            tens = 0
        else:
            tens=rolls[i,4]
    else:
        while rolls[i,4] == 6:
            rolls[i,4] = np.random.randint(1,7)
        tens=rolls[i,4] + 4
    rolled_numerals[i,2] = tens

    # ones, 10^1
    if rolls[i,5] <=3:
        while rolls[i,6] == 6:
            rolls[i,6] = np.random.randint(1,7)
        if rolls[i,6] == 5:
            ones = 0
        else:
            ones=rolls[i,6]
    else:
        while rolls[i,6] == 6:
            rolls[i,6] = np.random.randint(1,7)
        ones=rolls[i,6] + 4
    rolled_numerals[i,3] = ones

    # Here we convert from the numerals to a number consisting of the
    # thousands, hundreds, tens and ones numerals    
    rolled_value = int( str(rolled_numerals[i,0]) + str(rolled_numerals[i,1])
                       + str(rolled_numerals[i,2]) + str(rolled_numerals[i,3]))
    # Here we count how many times we roll each given number between 0 and 2999
    frequency_counter_d6[rolled_value] += 1
    

# This is not indented by tab, which means this part is after the loop rolling 
# all the numbers
# Below we calculate the average values for the thousands, hundreds, tens and
# ones numerals, just to check that they indeed are close to what they should 
# be:
# thousands can choose between 0, 1 and 2, and the average should then be 1
# For hundreds, tens and ones, the results can go from 0 to 9, with an average
# of 4.5
average_thousands = np.average( rolled_numerals[:, 0])      
average_hundreds = np.average( rolled_numerals[:, 1])
average_tens = np.average( rolled_numerals[:, 2])
average_ones = np.average( rolled_numerals[:, 3])            

print("Average values r, thousands: " + str(average_thousands) + 
      ", hundreds: " + str(average_hundreds) 
      + ", tens: " + str(average_tens) 
      + ", ones: " + str(average_ones))

# Testing the soundness of the generator
# Calculating the average frequency of all values, divided by the number
# of dice rolls, this should be 1/3000 = 0.0003333333333 and so on

average_frequency = np.average(frequency_counter_d6)
average_frequency_per_roll = average_frequency/no_rolls

# Will now calculate standard deviation of frequency per roll
# First deviation, is each frequency less the mean
frequency_deviation = frequency_counter_d6/no_rolls - average_frequency_per_roll
# The square of each deviation
frequency_deviations_squared = frequency_deviation*frequency_deviation
# The variance is the mean of the squared of the deviations
variance_d6 = np.average(frequency_deviations_squared)
# The standard deviation is the square root of the variance
standard_deviation_d6 = np.power(variance_d6, 0.5)

print("Standard deviation of frequency divided by average  " 
      +str(standard_deviation_d6 / average_frequency_per_roll))
print("Minimum of frequency: " + str(min(frequency_counter_d6)))
print("Maximum of frequency: " + str(max(frequency_counter_d6)))

# Adding average and standard deviation to the plot
frequency_deviations_value = frequency_counter_d6 - average_frequency
frequency_variance = np.average(frequency_deviations_value * frequency_deviations_value)
frequency_standard_deviation = np.math.sqrt(frequency_variance)

# Below we make the plot. 
# An important thing to note here is that the minimum and maximum values
# should show that no dice rolls where NOT rolled. If the minimum is zero,
# the algorithm has failed to roll some values.
plt.plot(frequency_counter_d6,'.', label="Frequency")
# plt.hlines(average_frequency, 0, 99, 'k', label="Average")
# plt.hlines(average_frequency+frequency_standard_deviation, 0, 99, 'k') #, label="Average + standard deviation")
# plt.hlines(average_frequency-frequency_standard_deviation, 0, 99, 'k', label="Standard deviation around average")
plt.hlines(min(frequency_counter_d6), 0, len(frequency_counter_d6), 'r', label="Minimum value")
plt.hlines(max(frequency_counter_d6), 0, len(frequency_counter_d6), 'g', label="Maximum value")
plt.legend(loc="best")
title = 'Frequency of rolled values from 0 to 2999 with %s' % no_rolls
title += ' rolls,\n the average value is %.2f ' % average_frequency
title += ' with a standard deviation of %.2f' %frequency_standard_deviation


plt.title(title)