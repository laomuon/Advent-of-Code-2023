import re

CARDS_VALUE = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


class CardHand:
    def __init__(self, cards: str, bid: str):
        self.cards = cards
        self.bid = int(bid)

    def _get_hand_type(self):
        different_cards = {}
        hand = self.cards
        for card in hand:
            if card not in different_cards:
                different_cards[card] = hand.count(card)

        if "J" not in different_cards:
            if len(different_cards) == 1:
                return 7
            if len(different_cards) == 2:
                for card_count in different_cards.values():
                    if card_count == 4:
                        return 6
                return 5
            if len(different_cards) == 3:
                for card_count in different_cards.values():
                    if card_count == 3:
                        return 4
                return 3
            if len(different_cards) == 4:
                return 2
            return 1
        else:
            if len(different_cards) in [1, 2]:
                return 7
            if len(different_cards) == 5:
                return 2
            if len(different_cards) == 4:
                return 4
            if len(different_cards) == 3:
                if different_cards["J"] in [2, 3]:
                    return 6
                for card_count in different_cards.values():
                    if card_count == 3:
                        return 6
                return 5

    def __lt__(self, other):
        if self._get_hand_type() < other._get_hand_type():
            return True
        if self._get_hand_type() > other._get_hand_type():
            return False
        for card_1, card_2 in zip(self.cards, other.cards):
            if CARDS_VALUE[card_1] < CARDS_VALUE[card_2]:
                return True
            if CARDS_VALUE[card_1] > CARDS_VALUE[card_2]:
                return False


def merge_sort(B, i_start, i_end, A):
    if i_end - i_start <= 1:
        return
    i_middle = int((i_end+i_start)/2)
    merge_sort(A, i_start, i_middle, B)
    merge_sort(A, i_middle, i_end, B)
    merge(B, i_start, i_middle, i_end, A)


def merge(B, i_start, i_middle, i_end, A):
    i = i_start
    j = i_middle
    k = i_start
    while (k < i_end):
        if (i < i_middle and (j >= i_end or A[i] < A[j])):
            B[k] = A[i]
            i = i + 1
        else:
            B[k] = A[j]
            j = j + 1
        k = k + 1


def part1(filename: str) -> int:
    hands = []
    ret = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            hand_bid = re.findall(r"\w+", line)
            if len(hand_bid) == 2:
                hands.append(CardHand(hand_bid[0], hand_bid[1]))

    sorted_hands = hands.copy()
    merge_sort(sorted_hands, 0, len(hands), hands)
    for i, c in enumerate(sorted_hands):
        ret += (i+1)*c.bid
    return ret


def part2(filename: str) -> int:
    hands = []
    ret = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            hand_bid = re.findall(r"\w+", line)
            if len(hand_bid) == 2:
                hands.append(CardHand(hand_bid[0], hand_bid[1]))

    sorted_hands = hands.copy()
    merge_sort(sorted_hands, 0, len(hands), hands)
    print({c.cards: c._get_hand_type() for c in sorted_hands if "J" in c.cards})
    for i, c in enumerate(sorted_hands):
        ret += (i+1)*c.bid
    return ret


if __name__ == "__main__":
    # print(f"Part 1 example: {part1('example')}")
    # print(f"Part 1 result: {part1('input')}")
    print(f"Part 2 example: {part2('example')}")
    print(f"Part 2 result: {part2('input')}")
