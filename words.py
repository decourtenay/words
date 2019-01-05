import glob
import string

file_list = glob.glob('files/word*.txt')
for letter in string.ascii_lowercase:
    counter = 0
    for filepath in file_list:
        file = open(filepath)
        word = file.readline()
        word = word.lower()
        for char in word:
            if char == letter:
                counter = counter + 1
    print(f"Litera \"{letter}\" występuje {counter} razy")