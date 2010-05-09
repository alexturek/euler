def number_combos_coins(coin_values, money_amount):
	"""Returns the number of coin combinations to make money_amount, using the coins specified in coin_values.

	number_combos_coins(set, int) -> int
	"""
	combos = list()
	coin_values = list(coin_values)
	coin_values.sort()
	min_value,max_value = min(coin_values),max(coin_values)
	combos.append([1 for i in range(min_value, money_amount+1)])

	# for each coin type, make a list of combos for each amount
	for coin_num in range(1,len(coin_values)):
		prev_coin_combos = combos[-1]
		coin_combos = [combos[coin_num-1][0]]
		combos.append(coin_combos)
		coin_value = coin_values[coin_num]
		for amt in range(min_value+1, money_amount+1):
			prev_coin_combo = prev_coin_combos[amt - min_value]

			diff = amt - coin_value
			prev_amt_combo = 0
			if diff > 0:
				prev_amt_combo = coin_combos[diff-1]
			elif diff == 0:
				prev_amt_combo = 1

			coin_combos.append(prev_coin_combo + prev_amt_combo)

	#print('\t'.join([str(i) for i in range(min_value, money_amount+1)]))
	#print('\n'.join(['\t'.join([str(c) for c in combo_row]) for combo_row in combos]))
	return combos[-1][-1]

english_money = [1, 2, 5, 10, 20, 50, 100, 200]

ans = number_combos_coins(english_money, 200)
