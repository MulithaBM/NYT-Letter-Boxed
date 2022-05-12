row_1 = "yor"
row_2 = "kha"

column_1 = "dei"
column_2 = "btc"

letters = row_1 + row_2 + column_1 + column_2
letter_set = set(letters)
dynamic_letter_set = set(letters)

letter_dict = {}

for letter in list(row_1) :
    letter_dict[letter] = "r1"

for letter in list(row_2) :
    letter_dict[letter] = "r2"

for letter in list(column_1) :
    letter_dict[letter] = "c1"

for letter in list(column_2) :
    letter_dict[letter] = "c2"

valid_words = []
words = []
sequence = []

def check_first_letter(start_letter, word) :
    if(start_letter == " " or start_letter == word[0]) :
        return True
    return False

def validate_letters(word) :
    if(set(word).issubset(letter_set)) :
        return True
    return False

def check_repetitive_letters(word) :
    for i in range(len(word) - 1) :
        if(word[i] == word[i + 1]) :
            return False
    return True

def check_consecutive_letters(word) :
    for i in range(len(word) - 1) :
        if(letter_dict[word[i]] == letter_dict[word[i + 1]]) :
            return False
    return True

def generate_word_sequence(start_letter) :
    for word in words :
        if(check_first_letter(start_letter, word)) :
            if(word not in sequence) :
                sequence.append(word)
                s = ' '.join(sequence)
                if(len(letter_set.difference(set(s))) == 0) :
                    valid_words.append(s)
                    sequence.remove(word)
                    return
                elif(len(sequence) >= 4) :
                    sequence.remove(word)
                    return
                else :
                    generate_word_sequence(word[-1])
                    sequence.remove(word)

file = open("US.txt", "r")
for line in file :
    word = line.rstrip()
    if(validate_letters(word) and (len(word) >= 3) and check_repetitive_letters(word) and check_consecutive_letters(word)) :
        words.append(word)
file.close()

words = sorted(words, key = lambda word, ls = letter_set : (len(set(word).intersection(ls))), reverse = True)

generate_word_sequence(" ")

valid_words = sorted(valid_words, key = lambda word : (word.count(' '), len(word)), reverse = True)

print(*valid_words, sep = "\n")