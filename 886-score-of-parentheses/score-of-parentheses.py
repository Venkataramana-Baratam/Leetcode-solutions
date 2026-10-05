class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        def fun(left, right):
            if right - left == 2:
                return 1

            balance = 0

            for i in range(left, right):
                if s[i] == '(':
                    balance += 1
                else:
                    balance -= 1

                if balance == 0:
                    if i == right - 1:
                        return 2 * fun(left + 1, right - 1)

                    return fun(left, i + 1) + fun(i + 1, right)

        return fun(0, len(s))