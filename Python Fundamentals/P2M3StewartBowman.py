# [] create poem mixer function, call the function with the provided test string
# [] test string: `Little fly, Thy summer’s play My thoughtless hand Has brushed away. Am not I A fly like thee? Or art not thou A man like me?`  
def word_mixer(word_list):
    word_list.sort()
    new_words = []
    while len(word_list)>5:
        new_words.append(word_list.pop(-5))
        new_words.append(word_list.pop(0))
        new_words.append(word_list.pop())
    else:
        return new_words

str_value = input("Welcome Stewart Bowman enter a poem or saying: ")
words_list = str_value.split()
length = len(words_list)
for index in range(0, length):
    if len(words_list[index])<=3:
        words_list[index] = words_list[index].lower()
    elif len(words_list[index])>=7:
        words_list[index] = words_list[index].upper()
print(" ".join(word_mixer(words_list)))