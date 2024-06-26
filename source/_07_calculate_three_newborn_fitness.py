import pandas as pd

from source.utils import chromo_action, chromo_count_matches, fitness_calculation

def calculate_three_newborn_fitness(df_op, df_ref_column, total_green, total_red, mutated_new_born_1, mutated_new_born_2, mutated_new_born_3):
	# Create dataframe with the three mutated newborns
	df_three_newborn = pd.DataFrame({'newborn 1': mutated_new_born_1, 'newborn 2': mutated_new_born_2, 'newborn 3': mutated_new_born_3})

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
		df_three_newborn_fitness[f'newborn {i+1} result'] = chromo_result
		i = i + 1

	# Create chromo reference: a DataFrame that contain
	# 'green' if number > 0 and 'red' if number < 0.
	df_three_newborn_fitness = df_three_newborn_fitness.applymap(lambda x: 'green' if x > 0 else 'red')

	# Calculate how many green's and how many red's were correct.
	df_three_newborn_fitness = df_three_newborn_fitness.apply(chromo_count_matches, ref_column=df_ref_column)

	# Calculate the fitness for all the six chromosome
	fitness_values = df_three_newborn_fitness.apply(fitness_calculation, args=(total_green, total_red))
	df_three_newborn_fitness.loc['fitness'] = fitness_values

	# Removing obsolete green and red rows
	i_remove = ['right green', 'right red']
	df_three_newborn_fitness = df_three_newborn_fitness.drop(i_remove)
	return df_three_newborn, df_three_newborn_fitness