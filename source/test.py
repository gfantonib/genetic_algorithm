from source.utils import chromo_action

def test(df_test, the_chosen_chromosome):
	the_chosen_chromosome_body = the_chosen_chromosome[1:].values
	scalar = the_chosen_chromosome[0]
	chromo_result = df_test.apply(func=chromo_action, axis=1, args=(the_chosen_chromosome_body, scalar))
	test_result = chromo_result.apply(lambda x: 'green' if x > 0 else 'red')
	return test_result