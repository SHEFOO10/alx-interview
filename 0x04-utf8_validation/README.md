# 0x04-utf8_validation

# Intuition
The problem requires us to validate whether a given array of integers represents a valid UTF-8 encoded sequence. UTF-8 encoding has specific rules for different byte lengths (1 to 4 bytes). By checking the leading bits of each byte, we can determine if the sequence follows the correct format.

# Approach
1. Define a helper function `calcBytes` to determine the number of leading 1s in a byte. This helps to identify the number of bytes in the current UTF-8 character.
2. Iterate through the data array:
   - For each byte, determine how many bytes the current character should have using `calcBytes`.
   - Check if the byte count is valid (not 1, not greater than 4).
   - Verify that the subsequent bytes (if any) start with `10` by ensuring they have exactly one leading 1.
3. If all checks pass, the data represents a valid UTF-8 encoding.

# Complexity
- Time complexity:
The time complexity is $$O(n)$$, where \(n\) is the length of the data array. Each byte is checked once.

- Space complexity:
The space complexity is $$O(1)$$ as no extra space is used beyond a few integer variables.
