class Solution:
    def intToRoman(self, num: int) -> str:
        
        roman_mapping = [
            (1000, "M"), (900, "CM"),
            (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"),
            (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"),
            (5, "V"), (4, "IV"),
            (1, "I")
        ]

        roman_result = []

        for decimal_value, roman_symbol in roman_mapping:
            if num == 0:
                break

            repeat_count, num = divmod(num, decimal_value)
            roman_result.append(roman_symbol * repeat_count)

        return "".join(roman_result)