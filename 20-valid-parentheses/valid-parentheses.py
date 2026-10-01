class Solution:
    def isValid(self, s: str) -> bool:

        st = []

        for ch in s:

            if ch in "([{":
                st.append(ch)

            else:
                if not st:
                    return False

                if  (ch == ')' and st[-1] == '(' ) or (ch == ']' and st[-1] == '[') or (ch == '}' and st[-1] == '{'):

                    st.pop()
                else:
                    return False

        return len(st) == 0