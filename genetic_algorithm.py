#!/usr/bin/env python3

import pandas as pd

from source._01_oil_database import oil_database
from source._02_create_firstborns import create_firstborns
from source._03_calculate_chromosomes_fitnes import calculate_chromosomes_fitnes
from source._04_elect_father_and_mother import elect_father_and_mother
from source._05_cross_and_birth_newborns import cross_and_birth_newborns
from source._06_mutate_the_three_newborns import mutate_the_three_newborns
from source._07_calculate_three_newborn_fitness import calculate_three_newborn_fitness
from source._08_select_new_lineage import select_new_lineage

i_max = int(input("Number of iteration: "))

# Read Excel file into a DataFrame.
df = pd.read_excel('data/data.xlsx')

# Set the seed for reproducibility
# np.random.seed(40)

df_op, df_ref_column, total_green, total_red, nbr_operatives_columns = oil_database(df)
df_current_lineage = create_firstborns(nbr_operatives_columns)

print(f"df_current_lineage before iteration:\n{df_current_lineage}\n")

i = 0
while (i < i_max):

	df_current_lineage_fitness = calculate_chromosomes_fitnes(df_op, df_current_lineage, df_ref_column, total_green, total_red)
	if i == 0:
		print(f"df_current_lineage_fitness before iteration:\n{df_current_lineage_fitness}\n")
	father_chromosome, mother_chromosome = elect_father_and_mother(df_current_lineage, df_current_lineage_fitness)
	new_born_1, new_born_2, new_born_3 = cross_and_birth_newborns(father_chromosome, mother_chromosome, nbr_operatives_columns)
	mutated_new_born_1, mutated_new_born_2, mutated_new_born_3 = mutate_the_three_newborns(df_current_lineage, new_born_1, new_born_2, new_born_3, nbr_operatives_columns)
	df_three_newborn, df_three_newborn_fitness = calculate_three_newborn_fitness(df_op, df_ref_column, total_green, total_red, mutated_new_born_1, mutated_new_born_2, mutated_new_born_3)
	df_new_lineage = select_new_lineage(df_current_lineage, df_current_lineage_fitness, df_three_newborn, df_three_newborn_fitness)
	df_current_lineage = df_new_lineage
	
	i = i + 1

print(f"df_current_lineage after iteration:\n{df_current_lineage}\n")
print(f"df_current_lineage_fitness after iteration:\n{df_current_lineage_fitness}\n")