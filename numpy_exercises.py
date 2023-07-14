import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are there?

# Created negative_num variable and assigned the sum method to sum all numbers in the array that are less than zero.
negative_nums = np.sum(a < 0)
print('Number of negative values = ', negative_nums, '\n')


# How many positive numbers are there?

# Created a positive_num variable and assigned the sum method to sum all numbers in the array that are greater than zero.
# 0 is neither a positive or a negative so its value is non-inclusive
positive_nums = np.sum(a > 0)
print('Number of positive values = ', positive_nums, '\n')


# How many even positive numbers are there?

# Created a even_positive_nums variable and assigned the sum method to sum all numbers in the array greater than 0 and divisible by 2 using the modulo operator.
# both conditions are applied usinf the '&' character after grouping each operation.
even_positive_nums = np.sum((a > 0) & (a % 2 == 0))
print('Number of even and postive numbers = ', even_positive_nums, '\n')

# If you were to add 3 to each data point, how many positive numbers would there be?

# assigned new variable with array values plus three and called back with a comparison to 0 and suffixed the sum() method using the '.' syntax
array_with_three_added = a + 3
print('Number of positive numbers with 3 added = ', (array_with_three_added > 0).sum(), '\n')

# If you squared each number, what would the new mean and standard deviation be?

# squared array values and then printed mean and standard deviation values using the numpy methods
a ** 2
print('Mean an standard deviation of array values squared:\n\n', 'Mean:', a.mean(), '\n\n STD:', a.std())


# A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.

# assigned variable centered_a to array subtracted by the array mean and printed the new array values by calling variable name
centered_a = a - a.mean()
print('\nCentered data:', centered_a, '\n')


# Calculate the z-score for each data point. Recall that the z-score is given by:

# z score is calculated by subtracting the array values the mean of arrays then divided by the standard deviation values of the array. 
# z_score was assigned to the calculation and returned when variable was called.
mean = np.mean(a)
std = np.std(a)

z_scores = (a - mean) / std
print("Z-scores:", z_scores)

# Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.