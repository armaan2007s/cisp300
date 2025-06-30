# This program reads and sums integers from a text file.

def sum_integers(text_file):
    sum = 0
    file = open(text_file, 'r')
    for line in file:
        for word in line.split():
            try:
                num = int(word)
                sum += num
            except ValueError:
                    continue
    print("The sum of the integers listed in the file is " + str(sum))

sum_integers('integers.txt')