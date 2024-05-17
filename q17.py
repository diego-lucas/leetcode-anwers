class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        buttons = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        
        def recursive(digits):
    
            if len(digits) >= 1:
                digit = digits[0]
                digits = digits[1:]
            else:
                return
            if len(result) == 0:
                result.extend(buttons[digit])
            else:
                temp = []
                possible_letters = buttons[digit]
                for item in result:
                    for letter in possible_letters:
                        temp.append(item+letter)
                result.clear()
                result.extend(temp)
            recursive(digits)
            
        result = []
        recursive(digits)
        return result
