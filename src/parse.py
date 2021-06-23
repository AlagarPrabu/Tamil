###
  # Tamil Character Parse
  # Copyright 2021 The Author Alagar Prabu
 ###
def get_characters(word):
    processed_character = []
    splitted_character = ""
    tamil_vowels = ["அ", "இ", "உ", "எ", "ஒ","ஆ", "ஈ", "ஊ", "ஏ", "ஐ", "ஓ", "ஔ", "ஃ"]
    tamil_consonent = ["க", "ங", "ச", "ஞ", "ட", "ண", "த","ந", "ப", "ம", "ய", "ர", "ல", "வ", "ழ", "ள", "ற", "ன","ஜ", "ஷ", "ஸ", "ஹ", "க்ஷ"]
    for get_character in word:
        if get_character in tamil_vowels:
            processed_character.append(get_character)
        elif get_character in tamil_consonent:
            if(splitted_character == ""):
                splitted_character += get_character
            else:
                processed_character.append(splitted_character)
                splitted_character = ""
                splitted_character += get_character
        else:
            splitted_character += get_character
            processed_character.append(splitted_character)
            splitted_character = ""
    if(splitted_character != ""):
        processed_character.append(splitted_character)
        splitted_character = ""

    return (processed_character)
