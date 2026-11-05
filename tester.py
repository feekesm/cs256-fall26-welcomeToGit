def num_vowels(input_text):
    ''' count and return the number of vowels in the input text'''
    count = 0
    for character in input_text:
        # check if character should be counted
        # assumes y is not a vowel
        if character.lower() in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count
