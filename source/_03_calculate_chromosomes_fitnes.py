import pandas as pd

from source.utils import chromo_action, chromo_count_matches, fitness_calculation

def calculate_chromosomes_fitnes(df_op, df_current_lineage, df_ref_column, total_green, total_red):
	# Iterate df_current_lineage in database.
	i = 0
	trash = None
	df_current_lineage_fitness = pd.DataFrame()
	max_i = len(df_current_lineage.columns)
	while i < max_i:
		current_chromosome = (df_current_lineage.iloc[1:, i]).values
		scalar = df_current_lineage.iloc[0, i]
		chromo_result = df_op.apply(func=chromo_action, axis=1, args=(current_chromosome, scalar))
		df_current_lineage_fitness[f'chromo {i+1} result'] = chromo_result
		i = i + 1

	# Create chromo reference: a DataFrame that contain
	# 'A' if number > 0 and 'I' if number < 0.
	df_current_lineage_fitness = df_current_lineage_fitness.applymap(lambda x: 'green' if x > 0 else 'red')
	df_current_lineage_fitness = df_current_lineage_fitness.apply(chromo_count_matches, ref_column=df_ref_column)
	fitness_values = df_current_lineage_fitness.apply(fitness_calculation, args=(total_green, total_red))
	df_current_lineage_fitness.loc['fitness'] = fitness_values

	# Removing obsolete A and I rows
	i_remove = ['right green', 'right red']
	df_current_lineage_fitness = df_current_lineage_fitness.drop(i_remove)
	return df_current_lineage_fitness