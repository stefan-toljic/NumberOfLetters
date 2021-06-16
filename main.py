"""
2. Number of letters

Ask user to enter a sentence. Write number of occurrences of letter A in the string (both upper-case and lower-case letters should be counted).
"""

user_input = input("Please enter a sentence:\n\t").lower()

occurrences = 0

for letter in user_input:
    if letter == 'a':
        occurrences += 1

print(f"\n- The number of times letter 'A' appears is {occurrences}.")

# --------------------------------------------------------------------
