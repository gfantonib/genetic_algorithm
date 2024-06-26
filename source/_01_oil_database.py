def oil_database(df):
	# Remove column.
	df = df.drop(columns=['Unnamed: 0'])

	# Change column name.
	df = df.rename(columns={'Unnamed: 19': 'reference'})

	# Create column of reference with A and I.
	df_ref_column = df['reference']

	# Store the DataFrame reference of A's and I's in a int.
	total_A = df["reference"].value_counts()["A"]
	total_I = df["reference"].value_counts()["I"]

	# Define operative DataFrame:
	# with the columns from X11 to X92, without reference column.
	df_op = df.loc[:, "X11": "X92"]

	# Count the number of operatives columns (between X11 and X92).
	nbr_operatives_columns = len(df_op.columns)
	return df_op, df_ref_column, total_A, total_I, nbr_operatives_columns