#!/usr/bin/env python3

import pandas as pd

from source._01_oil_database import oil_database, init_variables
from source._02_create_firstborns import create_firstborns
from source.train import train
from source.test import test

i_max = int(input("Number of iteration: "))
testing = int(input("Do you want to run with test?\n(1 for yes and 0 for no): "))

# Read Excel file into a DataFrame.
# df = pd.read_excel('data/data.xlsx')
# df_op, df_ref_column, total_green, total_red, nbr_operatives_columns = oil_database(df)

# Training
df_train = pd.read_csv('data/oiled_titanic_data_train.csv')
df_op, df_ref_column, total_green, total_red, nbr_operatives_columns = init_variables(df_train)
df_current_lineage = create_firstborns(nbr_operatives_columns)
the_chosen_chromosome = train(i_max, df_op, df_ref_column, total_green, total_red, nbr_operatives_columns, df_current_lineage)

# Testing
if testing:
	df_test = pd.read_csv('data/oiled_titanic_data_test.csv')
	test_result = test(df_test, the_chosen_chromosome)
	test_result.to_pickle("test_result.pkl")