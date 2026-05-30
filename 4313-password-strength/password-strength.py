class Solution:
    def passwordStrength(self, password: str) -> int:

        lower = set()
        upper = set()
        digit = set()
        special = set()

        for ch in password:

            if ch.islower():
                lower.add(ch)

            elif ch.isupper():
                upper.add(ch)

            elif ch.isdigit():
                digit.add(ch)

            elif ch in "!@#$":
                special.add(ch)

        return len(lower) + 2 * len(upper) + 3 * len(digit) + 5 * len(special)