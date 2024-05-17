class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters_no_repeat = []
        longest_string_size = 0

        for letter in s:
            if letter not in letters_no_repeat:
                letters_no_repeat.append(letter)
            else:
                letters_no_repeat = letters_no_repeat[(letters_no_repeat.index(letter)+1):]
                letters_no_repeat.append(letter)
            if len(letters_no_repeat) > longest_string_size:
                longest_string_size = len(letters_no_repeat)
                
        return longest_string_size
                
