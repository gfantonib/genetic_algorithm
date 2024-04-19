import numpy as np

# raffle function: it resturn a position given a raffle number.
def get_raffle_point(raffle, norm_fitness_array):
	max_i = len(norm_fitness_array) -1
	i = 0
	while i < max_i:
		if 0 <= raffle <= norm_fitness_array[0]:
			return 0
		elif norm_fitness_array[i] < raffle <= norm_fitness_array[i + 1]:
			return i
		i = i + 1
	return 0

def elect_father_and_mother(df_current_lineage, df_current_lineage_fitness):
	# Get two raffle points to choose two chromosomes.
	# The choosen chromosomes are going to be crossed.

	# Create array with fitness values.
	fitness_array = (df_current_lineage_fitness.iloc[0, :]).values

	# Sum the array.
	fitness_array_sum = fitness_array.sum()

	# Create new array with cumulative sum.
	norm_fit_0 = round((fitness_array[0]/ fitness_array_sum) * 100)
	norm_fit_1 = round((fitness_array[1]/ fitness_array_sum) * 100) + norm_fit_0
	norm_fit_2 = round((fitness_array[2]/ fitness_array_sum) * 100) + norm_fit_1
	norm_fit_3 = round((fitness_array[3]/ fitness_array_sum) * 100) + norm_fit_2
	norm_fit_4 = round((fitness_array[4]/ fitness_array_sum) * 100) + norm_fit_3
	norm_fit_5 = round((fitness_array[5]/ fitness_array_sum) * 100) + norm_fit_4
	norm_fitness_array = np.array([norm_fit_0, norm_fit_1, norm_fit_2, norm_fit_3, norm_fit_4, norm_fit_5])
	# norm_fitness_array[5] = 1 (this value must be equal to one).
	# This is not used, is just a check.

	# Get two raffle points given a random raffle.
	raffle_1 = round(np.random.random() * 100)
	raffle_point_1 = get_raffle_point(raffle_1, norm_fitness_array)
	raffle_2 = round(np.random.random() * 100)
	raffle_point_2 = get_raffle_point(raffle_2, norm_fitness_array)

	# Selec (from the random above) a mother and a father chromosome.
	father_chromosome = df_current_lineage.iloc[:, raffle_point_1]
	mother_chromosome = df_current_lineage.iloc[:, raffle_point_2]
	return (father_chromosome, mother_chromosome)