"""
input: groupSize = size of every group
       hand = hand[i] = value of ith card

output: boolean -> true if can rearrange cards, false otherwise




"""


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hm = Counter(hand)
        hand.sort()

        for i in hand:
            if hm[i] == 0:
                continue
            for j in range(groupSize):
                if hm[i + j] == 0:
                    return False
                hm[i + j] -= 1

        return True


        