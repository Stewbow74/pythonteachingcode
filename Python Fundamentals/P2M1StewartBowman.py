def test_words_after_g():
    sentence = input("Welcome Stewart Bowman. Enter a 1 sentence quote, non-alpha separated words: ").upper()+" "
    word = ""
    for letter in sentence:
        if letter.isalpha():
            word += letter
        if letter == " ":
            if word[0] >= "H":
                print(word)
                word = ""
            elif word[0] <= "G":
                word = ""
        
test_words_after_g()