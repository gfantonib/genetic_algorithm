import pandas as pd
import numpy as np

# Function to aply each chromosome for each line of the DataFrame
# and return the result (line * chromosome).sum().
def chromo_action(row, current_chromosome, scalar):
	res_mult = row * current_chromosome
	res_sum = res_mult.sum() + scalar
	return (res_sum)

# Calculate how many A's and how many I's were correct.
def chromo_count_matches(column, ref_column):
	relative_A = ((column == 'A') & (ref_column == 'A')).sum()
	relative_I = ((column == 'I') & (ref_column == 'I')).sum()
	return pd.Series({'right A': relative_A, 'right I': relative_I})

# Calculate the fitness for all the six chromosome
def fitness_calculation(column, total_A, total_I):
	relative_numerator = np.prod(column)
	fitness = relative_numerator / (total_A * total_I)
	return fitness