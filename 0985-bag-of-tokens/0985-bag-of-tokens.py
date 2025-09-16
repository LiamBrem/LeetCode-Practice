class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        l, r = 0, len(tokens) - 1

        score = 0


        while l <= r:
            if tokens[l] <= power:
                # "buy" tokens and decrease power
                power -= tokens[l]
                score += 1
                l += 1

            elif score >= 1 and l != r:
                # gain as much power as possible
                power += tokens[r]
                score -=1
                r -= 1 

            else:
                # no moves less
                break


        return score