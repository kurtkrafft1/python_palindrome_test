user_input = input('Please enter a word or a sentence and I will tell you if it is a palindrome. ')

def p_test(user_phrase):
    word = user_phrase.lower()
    for character in word:
        if character.isdigit():
            print("Please no numbers")
            return 
    for character in word:
        if not character.isalnum():
            if character != " ":
                print('Please no symbols')
                return 
    reversed = word[::-1]
    if reversed == word:
        print('Yes! it is a palindrome')
    else:
        print('lol nope, not a palindrome')

p_test(user_input)