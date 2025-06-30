# This program gives frequency of each word in the file.

def file_word_frequency(filename):
    text = open(filename, 'r').read()
    
    words = text.lower().split()
    counted = []

    for word in words:
        if word not in counted:
            count = words.count(word)
            counted.append(word)
            print(word + " : " + str(count))

file_word_frequency('words.txt')