from collections import defaultdict

order = '23456789TJQKA'
card_values = {L:order.index(L) for L in order}

def cards(hand):
	return hand.split(' ')
    
def values(_cards):
	card_key = card_values.__getitem__
	return ''.join(sorted((c[0] for c in _cards), key=card_key, reverse=True))
    
def suits(_cards):
	return ''.join(sorted((c[1] for c in _cards)))

def rule_high_card(hand1, hand2):
	vals1 = tuple(card_values[v] for v in values(cards(hand1)))
	vals2 = tuple(card_values[v] for v in values(cards(hand2)))
	return vals1 > vals2

def rule_pair(hand1,hand2):
	pass
