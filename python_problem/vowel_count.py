#vowel count
def get_vowels(s):
    vowels = "aeiou"
    vowel_list = list(filter(lambda x: x in vowels, s))
    return vowel_list, len(vowel_list)

result, count = get_vowels("quintessential")
print(result, ";", count)
