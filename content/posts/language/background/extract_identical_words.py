dutch_list = []
f = open("10000_words_dutch.md", "r")

for x in f:
    dutch_list.append(str.strip(x))
f.close()

german_list = []
f = open("10000_words_german.md", "r")
for x in f:
    german_list.append(str.strip(x))
f.close()

list_identical_words = list(set(german_list).intersection(set(dutch_list)))

print(list_identical_words)

textfile = open("results_file.txt", "w")
for element in list_identical_words:
    textfile.write(element + "\n")
textfile.close()
