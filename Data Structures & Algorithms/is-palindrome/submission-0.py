class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = []
        for i in range(0, len(s)):
            if (s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= '0' and s[i] <= '9'):
                output.append(s[i].lower())
        
        reversed_output = output[::-1]

        if reversed_output == output:
            return True
        else:
            return False