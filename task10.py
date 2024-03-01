def replace_vowels(string, vowel):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    new_string = ''.join(vowel if c in vowels else c for c in string)

    return new_string


print(replace_vowels("apples and bananas", 'u'))  # Output: "Hxllx, Wxrld!"
