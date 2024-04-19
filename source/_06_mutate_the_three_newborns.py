import numpy as np
import copy

# Function to mutate a given new born.
def mutate_newborn(new_born, random_value, nbr_operatives_columns):
	mutation_point = round(nbr_operatives_columns * np.random.random())
	mutated_new_born = copy.deepcopy(new_born)
	mutated_new_born[mutation_point] = random_value
	return mutated_new_born

# Get random a single value from all the current_lineage database.
def get_random_value(df_current_lineage):
	# Select a random row
	random_row = df_current_lineage.sample()
	# Select a random column
	random_column = np.random.choice(df_current_lineage.columns)
	# Get the value at the random row and random column
	random_value = random_row[random_column].values[0]
	return random_value

def mutate_the_three_newborns(df_current_lineage, new_born_1, new_born_2, new_born_3, nbr_operatives_columns):
	# Mutating the three new borns
	random_value = get_random_value(df_current_lineage)
	mutated_new_born_1 = mutate_newborn(new_born_1, random_value, nbr_operatives_columns)
	random_value = get_random_value(df_current_lineage)
	mutated_new_born_2 = mutate_newborn(new_born_2, random_value, nbr_operatives_columns)
	random_value = get_random_value(df_current_lineage)
	mutated_new_born_3 = mutate_newborn(new_born_3, random_value, nbr_operatives_columns)
	return mutated_new_born_1, mutated_new_born_2, mutated_new_born_3