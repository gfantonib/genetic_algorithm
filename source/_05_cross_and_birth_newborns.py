import numpy as np

# cross function: it cross a father and a mother and generates a new born that
# is part mother and part father. The crossing point is random.
def cross_father_mother(father, mother, nbr_operatives_columns):
	cross_point = round(nbr_operatives_columns * np.random.random())
	paternal_sperm  = father[cross_point:]
	maternal_egg = mother[:cross_point]
	new_born = np.hstack((maternal_egg, paternal_sperm))
	return (new_born)

def cross_and_birth_newborns(father_chromosome, mother_chromosome, nbr_operatives_columns):
	# Create 3 new borns with the same father and mother.
	new_born_1 = cross_father_mother(father_chromosome.values, mother_chromosome.values, nbr_operatives_columns)
	new_born_2 = cross_father_mother(father_chromosome.values, mother_chromosome.values, nbr_operatives_columns)
	new_born_3 = cross_father_mother(father_chromosome.values, mother_chromosome.values, nbr_operatives_columns)
	return (new_born_1, new_born_2, new_born_3)