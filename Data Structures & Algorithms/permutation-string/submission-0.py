class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_dict = {}
        s2_dict = {}

        for char in s1:
            s1_dict[char] = s1_dict.get(char, 0) + 1

        k = len(s1)

        # Initialize the first window of length k in s2
        for i in range(k):
            s2_dict[s2[i]] = s2_dict.get(s2[i], 0) + 1

        if s1_dict == s2_dict:
            return True

        # Slide the window across s2
        for i in range(k, len(s2)):
            # Add new incoming character
            s2_dict[s2[i]] = s2_dict.get(s2[i], 0) + 1

            # Remove character going out of window
            outgoing_char = s2[i - k]
            s2_dict[outgoing_char] -= 1
            if s2_dict[outgoing_char] == 0:
                del s2_dict[outgoing_char]

            # Check if current window matches s1's frequency
            if s1_dict == s2_dict:
                return True

        return False