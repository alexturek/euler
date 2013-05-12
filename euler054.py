from collections import defaultdict
import itertools as it
import unittest as ut

cardmap = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12, 'C': 'b', 'D': 'c', 'H': 'd', 'S': 'a'}
hand_order = {'s': 6, 'k2': 3, 'k4': 9, 'k3': 5, 'p2': 4, 'f': 7, 'hc': 2, 'sf': 10, 'fh': 8}
hand_names = {
10:"straight flush",
9: "4 of a kind   ",
8: "full house    ",
7: "flush         ",
6: "straight      ",
5: "3 of a kind   ",
4: "2 pair        ",
3: "one pair      ",
2: "high card     "}

class PositiveCases(ut.TestCase):
    def test_high_card(self):
        hand = [(10,'a'),(9,'a'),(2,'a'),(4,'b'),(5,'a')]
        sco = score(hand)
        self.assertEqual(hand_order['hc'], sco[0])
        self.assertEqual((10,9,5,4,2), tuple(sco[1]))
    def test_one_pair(self):
        hand = [(2,'a'),(9,'a'),(2,'a'),(4,'b'),(5,'a')]
        sco = score(hand)
        self.assertEqual(hand_order['k2'], sco[0])
        self.assertEqual((2,2,9,5,4), tuple(sco[1]))
    def test_two_pair(self):
        hand = [(10,'a'),(5,'a'),(10,'a'),(4,'b'),(5,'a')]
        sco = score(hand)
        self.assertEqual(hand_order['p2'], sco[0])
        self.assertEqual((10,10,5,5,4), tuple(sco[1]))
    def test_three_kind(self):
        hand = [(10,'a'),(5,'a'),(5,'a'),(4,'b'),(5,'a')]
        sco = score(hand)
        self.assertEqual(hand_order['k3'], sco[0])
        self.assertEqual((5,5,5,10,4), tuple(sco[1]))
    def test_straight_normal(self):
        hand = [(7,'a'),(5,'a'),(6,'a'),(4,'b'),(3,'a')]
        sco = score(hand)
        self.assertEqual(hand_order['s'], sco[0])
        self.assertEqual((7,6,5,4,3), tuple(sco[1]))
    def test_straight_ace(self):
        hand = [(12,'a'),(0,'a'),(1,'a'),(2,'b'),(3,'a')]
        sco = score(hand)
        self.assertEqual(hand_order['s'], sco[0])
        self.assertEqual((12,3,2,1,0), tuple(sco[1]))
    def test_flush(self):
        hand = [(10,'a'),(5,'a'),(9,'a'),(4,'a'),(5,'a')]
        sco = score(hand)
        self.assertEqual(hand_order['f'], sco[0])
        self.assertEqual((10,9,5,5,4), tuple(sco[1]))
    def test_four_kind(self):
        hand = [(10,'a'),(5,'a'),(5,'a'),(5,'b'),(5,'a')]
        sco = score(hand)
        self.assertEqual(hand_order['k4'], sco[0])
        self.assertEqual((5,5,5,5,10), tuple(sco[1]))
    def test_full_house(self):
        hand = [(10,'a'),(5,'a'),(10,'a'),(5,'b'),(5,'a')]
        sco = score(hand)
        self.assertEqual(hand_order['fh'], sco[0])
        self.assertEqual((5,5,5,10,10), tuple(sco[1]))
    def test_straight_flush(self):
        hand = [(1,'a'),(5,'a'),(2,'a'),(4,'a'),(3,'a')]
        sco = score(hand)
        self.assertEqual(hand_order['sf'], sco[0])
        self.assertEqual((5,4,3,2,1), tuple(sco[1]))

def halves(s):
    hl = len(s)//2
    return s[:hl],s[hl:]
def normalize(str_hand):
    mapped = [cardmap[L] for L in str_hand]
    hand = list(zip(mapped[0::2], mapped[1::2]))
    # print("normalizing",str_hand,"to",hand)
    return hand
def listdiff(L):
    return tuple([L[i]-L[i+1] for i in range(len(L)-1)])
def big_to_small(counts):
    counts = sorted(counts)
    counts.reverse()
    return counts
def card_counts(hand):
    cards = defaultdict(int)
    for card in hand:
        cards[card[0]] += 1
    return cards
def freq_count(counts):
    freqs = [[] for i in range(6)]
    for k in counts:
        v = counts[k]
        freqs[v].append(k)
    for ranks in freqs:
        ranks.sort()
        ranks.reverse()
    return freqs
def hands(line):
    line = ''.join(line.strip().split(' '))
    cards1,cards2 = halves(line)
    return normalize(cards1),normalize(cards2)
def sf(hand, counts, freqs):
    _s = s(hand, counts, freqs)
    _f = f(hand, counts, freqs)
    if _s and _f:
        return hand_order["sf"], big_to_small(counts)
def s(hand, counts, freqs):
    o = big_to_small(counts)
    if listdiff(o) in {(1,1,1,1), (9,1,1,1)}:
        return hand_order["s"], o
def f(hand, counts, freqs):
    if len(set(c[1] for c in hand)) == 1:
        return hand_order["f"], [c[0] for c in big_to_small(hand)]
def _kind(num, lookup, min_freq):
    def hand_func(hand, counts, freqs):
        kinds = freqs[num]
        if len(kinds) >= min_freq:
            leftovers = big_to_small(list(filter(lambda x: x not in kinds, counts)))
            # print(leftovers,"are left over")
            allsets = list(it.chain(*([k] * num for k in kinds)))
            # print(allsets,'all sets')
            return hand_order[lookup], allsets + leftovers
    return hand_func
def fh(hand, counts, freqs):
    if len(freqs[3]) == len(freqs[2]) == 1:
        return hand_order["fh"], tuple([freqs[3][0]] * 3 + [freqs[2][0]] * 2)
def hc(hand, counts, freqs):
    return hand_order["hc"], tuple(c[0] for c in big_to_small(hand))
k4 = _kind(4, "k4", 1)
k3 = _kind(3, "k3", 1)
k2 = _kind(2, "k2", 1)
p2 = _kind(2, "p2", 2)

score_order = [sf, k4, fh, f, s, k3, p2, k2, hc]
def score(hand):
    counts = card_counts(hand)
    freqs = freq_count(counts)
    for hand_type in score_order:
        sc = hand_type(hand, counts, freqs)
        if sc != None:
            return sc

player1_underline = "--------------"
player2_underline = "               --------------"
if __name__ == "__main__":
    with open("/projects/poker.txt", 'r') as gamefile:
        lines = gamefile.readlines()
    player1_wins = 0
    #lines = ["7D 5D TS 9H 4H 4C 9C 2H 8C QC"]
    for line in lines:
        print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
        h1,h2 = hands(line)
        s1,s2 = score(h1),score(h2)
        if s1 > s2:
            print(line.strip())
            print(player1_underline)
            print(hand_names[s1[0]], hand_names[s2[0]])
            print()
            player1_wins += 1
        else:
            print(line.strip())
            print(player2_underline)
            print(hand_names[s1[0]], hand_names[s2[0]])
            print()
    print("Player 1 wins:",player1_wins)