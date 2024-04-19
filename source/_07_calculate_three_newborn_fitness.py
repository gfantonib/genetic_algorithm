import pandas as pd

from source.utils import chromo_action, chromo_count_matches, fitness_calculation

def calculate_three_newborn_fitness(df_op, df_ref_column, total_A, total_I, mutated_new_born_1, mutated_new_born_2, mutated_new_born_3):
	# Create dataframe with the three mutated newborns
	df_three_newborn = pd.DataFrame({'Newborn 1': mutated_new_born_1, 'Newborn 2': mutated_new_born_2, 'Newborn 3': mutated_new_born_3})

	# Apply the same fitness flow to the new dataframe with the newborns

	# Iterate df_current_lineage in database.
	i = 0
	trash = None
	df_three_newborn_fitness = pd.DataFrame()
	max_i = len(df_three_newborn.columns)
	while i < max_i:
		current_chromosome = (df_three_newborn.iloc[1:, i]).values
		scalar = df_three_newborn.iloc[0, i]
		chromo_result = df_op.apply(func=chromo_action, axis=1, args=(current_chromosome, scalar))
		df_three_newborn_fitness[f'Newborn {i+1} result'] = chromo_result
		i = i + 1

	# Create chromo reference: a DataFrame that contain
	# 'A' if number > 0 and 'I' if number < 0.
	df_three_newborn_fitness = df_three_newborn_fitness.applymap(lambda x: 'A' if x > 0 else 'I')

	# Calculate how many A's and how many I's were correct.
	df_three_newborn_fitness = df_three_newborn_fitness.apply(chromo_count_matches, ref_column=df_ref_column)

	# Calculate the fitness for all the six chromosome
	fitness_values = df_three_newborn_fitness.apply(fitness_calculation, args=(total_A, total_I))
	df_three_newborn_fitness.loc['Fitness'] = fitness_values

	# Removing obsolete A and I rows
	i_remove = ['Right A', 'Right I']
	df_three_newborn_fitness = df_three_newborn_fitness.drop(i_remove)
	return df_three_newborn, df_three_newborn_fitness