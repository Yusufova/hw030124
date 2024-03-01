def are_anagrams(str1, str2):
    # Convert strings to lowercase and remove spaces
    str1 = str1.lower()
    str2 = str2.lower()
    h = sorted(str1) == sorted(str2)

    return h


# Test the function
print(are_anagrams('cristian', 'Cristina'))  # True
print(are_anagrams('nope', 'note'))  # False
