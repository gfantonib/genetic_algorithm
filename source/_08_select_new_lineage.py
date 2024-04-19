import pandas as pd

def select_new_lineage(df_current_lineage, df_current_lineage_fitness, df_three_newborn, df_three_newborn_fitness):
	# Choose the best two between the three newborns
	min_column_name = (df_three_newborn_fitness.min().idxmin())
	min_column_name = df_three_newborn_fitness.columns.get_loc(min_column_name)
	df_three_newborn_less_one = df_three_newborn.drop(df_three_newborn.columns[min_column_name], axis=1)

	# Remove the worst two between the six from the current lineage
	df_current_lineage_fitness_stacked = df_current_lineage_fitness.stack()
	smallest_indices = df_current_lineage_fitness_stacked.nsmallest(2).index
	min_column_index_one = df_current_lineage_fitness.columns.get_loc(smallest_indices[0][1])
	min_column_index_two = df_current_lineage_fitness.columns.get_loc(smallest_indices[1][1])
	df_current_lineage_less_two = df_current_lineage.drop(df_current_lineage.columns[[min_column_index_one, min_column_index_two]], axis=1)

	# Create new lineage by joining the two best from the newborns and the four best from the current lineage
	df_new_lineage = pd.concat([df_current_lineage_less_two, df_three_newborn_less_one], axis=1)
	new_columns_names = ['chromo_1', 'chromo_2', 'chromo_3', 'chromo_4', 'chromo_5', 'chromo_6']
	df_new_lineage.columns = new_columns_names
	return df_new_lineage
