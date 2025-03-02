
def countchar(str):

    vowels = "aiuoeAIUOE"
    vowel = 0
    consonant = 0
    digits = 0
    space = 0

    for item in str:

        if item in vowels:
            vowel += 1
        elif item.isalpha():
            consonant += 1
        elif item.isdigit():
            digits += 1
        else:
            space += 1

    print(f"Vowels {vowel}\n Consonants {consonant}\n Digits {digits}\n WhiteSpac {space}")

usr_in = input("Enter your string ")
countchar(usr_in)
