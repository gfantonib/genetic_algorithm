import pandas as pd
import numpy as np

def create_firstborns(nbr_operatives_columns):
	# Create firstborns (chromosomes).

	# Generate 6 random chromosomes.
	chromosome1 = -1 + 2 * np.random.random(nbr_operatives_columns + 1) # +1 for the scalar
	chromosome2 = -1 + 2 * np.random.random(nbr_operatives_columns + 1)
	chromosome3 = -1 + 2 * np.random.random(nbr_operatives_columns + 1)
	chromosome4 = -1 + 2 * np.random.random(nbr_operatives_columns + 1)
	chromosome5 = -1 + 2 * np.random.random(nbr_operatives_columns + 1)
	chromosome6 = -1 + 2 * np.random.random(nbr_operatives_columns + 1)

	# Create re-usable DataFrame with the current lineage
	df_current_lineage = pd.DataFrame({
										'chromo 1':chromosome1,
										'chromo 2':chromosome2,
										'chromo 3':chromosome3,
										'chromo 4':chromosome4,
										'chromo 5':chromosome5,
										'chromo 6':chromosome6})
	return df_current_lineage