def check_first_letter(start_letter, word) :
    if(start_letter == "" or start_letter == word[0]) :
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

# Check if the adjecent letter is from the same row or column
def check_consecutive_letters(word) :
    for i in range(len(word) - 1) :
        if(letter_dict[word[i]] == letter_dict[word[i + 1]]) :
            return False
    return True

def generate_word_sequence(start_letter) :
    for word in words :
        if((check_first_letter(start_letter, word)) and (word not in sequence_array)) :
            sequence_array.append(word)
            sequence = ' '.join(sequence_array)
            if(len(letter_set.difference(set(sequence))) == 0) :
                valid_sequence.append(sequence)
                global sequence_length
                sequence_length = len(sequence_array)
                sequence_array.remove(word)
                return
            elif(len(sequence_array) >= sequence_length) :
                sequence_array.remove(word)
                return
            else :
                generate_word_sequence(word[-1])
                sequence_array.remove(word)

words = []

row_1 = input("Row 1 : ")
row_2 = input("Row 2 : ")
column_1 = input("Column 1 : ")
column_2 = input("Column 2 : ")

letters = row_1 + row_2 + column_1 + column_2
letter_set = set(letters)

letter_dict = {}

for letter in list(row_1) :
    letter_dict[letter] = "r1"

for letter in list(row_2) :
    letter_dict[letter] = "r2"

for letter in list(column_1) :
    letter_dict[letter] = "c1"

for letter in list(column_2) :
    letter_dict[letter] = "c2"

valid_sequence = []
sequence_array = []

sequence_length = 6

file = open("US.txt", "r")
for line in file :
    word = line.rstrip()
    if(validate_letters(word) and (len(word) >= 3) and check_repetitive_letters(word) and check_consecutive_letters(word)) :
        words.append(word)
file.close()

words = sorted(words, key = lambda word, ls = letter_set : (len(set(word).intersection(ls))), reverse = True)

generate_word_sequence("")

# Reverse sorted ordered according to the number of words and length of those words (Desc.)
valid_sequence = sorted(valid_sequence, key = lambda word : (word.count(' '), len(word)), reverse = True)

# For a list of sequences
# print(*valid_sequence, sep = "\n")

print(valid_sequence[-1])
