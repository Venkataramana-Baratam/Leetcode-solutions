class Solution(object):
    def pushDominoes(self, dominoes):
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in range(i + 1, j):
                    ans[k] = x
            elif x == 'R' and y == 'L':  # RL
                for k in range(i + 1, j):
                    cmp_val = (k - i > j - k) - (k - i < j - k)
                    ans[k] = '.LR'[cmp_val]

        return "".join(ans)
