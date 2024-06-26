def oil_database(df):
	# Remove column.
	df = df.drop(columns=['Unnamed: 0'])

	# Change column name.
	df = df.rename(columns={'Unnamed: 19': 'reference'})

	# Change A to green and I to red
	df['reference'] = df['reference'].apply(
	lambda x: "green" if x == "A" 
	else "red")

	# Create column of reference with green and red.
	df_ref_column = df['reference']

	# Store the DataFrame reference of green's and red's in a int.
	total_green = df["reference"].value_counts()["green"]
	total_red = df["reference"].value_counts()["red"]

	# Define operative DataFrame:
	# with the columns from X11 to X92, without reference column.
	df_op = df.loc[:, "X11": "X92"]

	# Count the number of operatives columns (between X11 and X92).
	nbr_operatives_columns = len(df_op.columns)
	return df_op, df_ref_column, total_green, total_red, nbr_operatives_columns

def init_variables(df):
	# Create column of reference with green and red.
	df_ref_column = df['reference']

	# Store the DataFrame reference of green's and red's in a int.
	total_green = df["reference"].value_counts()["green"]
	total_red = df["reference"].value_counts()["red"]

	# Define operative DataFrame:
	# with the columns from X11 to X92, without reference column.
	ref_column_index = df.columns.get_loc("reference")
	df_op = df.iloc[:, :ref_column_index]

	# Count the number of operatives columns (between X11 and X92).
	nbr_operatives_columns = len(df_op.columns)
	return df_op, df_ref_column, total_green, total_red, nbr_operatives_columns
