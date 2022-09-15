infile = open('sometext.txt', 'r')

word_count = {}

# cleans up the text
x = infile.read().replace('.','').replace(',','').lower()

for word in x.split():
    word_count[word] = x.count(word)

# storing numbers in .txt file in the list to remove numbers later
number_list = []

# finding the numbers and appending
for word in word_count:
    try:
        if int(word) > 0:
            number_list.append(word)
    except ValueError:
        pass

# removing the numbers
for number in number_list:
    del word_count[number]

for word in sorted(word_count):
    print(f'"{word}" appears {word_count[word]} time(s)')
