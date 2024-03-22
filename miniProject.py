import json
import difflib as dl
data = json.load(open('data.json'))

word = input('Enter a word: ').lower()
t = []
for c in data:
	t.append(c)
findword = dl.get_close_matches(word, t)
def dictionary(searchword):
    for x in data:
        if x == searchword:
            print(f'The meaning of {searchword} is: ', data[x][0].replace('[', '').replace(']', ''))
    if searchword not in data:
        print('Word not available')

dictionary(findword[0])
