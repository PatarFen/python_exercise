import re

f = open("4.txt","r")

content_lines = f.readlines()

words_set = set()

for i in content_lines:
    words = re.split('\W+',i)
    for j in words:
        if j != '':
            words_set.add(j)

print(len(words_set))