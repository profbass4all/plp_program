import json
data = json.load(open('data.json'))

word = input('Enter a word: ').lower()
def dictionary(word):
    for x in data:
        if x == word:
            print(data[x][0].replace('[', '').replace(']', ''))
    if word not in data:
        print('Word not available')

dictionary(word)
