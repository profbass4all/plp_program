#Task 1
# given = []

# length = int(input('Please enter a length of list: '))
# i = 0
# while i < length:
#     intake = int(input('Please enter a number: '))
#     given.append(intake)
#     i += 1
# total = 0
# for x in given:
#     total += x

# print(total)

#Task 2
# books = ('bookA', 'bookB', 'bookC', 'bookD', 'bookE')
# for x in books:
#     print(x)

x = {'b': 4, 'c':32}
if 'c' in x:
    print('in there')

#Task 3
# dictPerson = {}
# dictPerson['name'] = input('What is your name: ')
# dictPerson['age'] = input('What is your age? ')
# dictPerson['favColor'] = input('What is your favourite color? ')

# print(dictPerson)

#Task 4
# mySet1 = set(())
# length1 = int(input('Please enter a length for set 1: '))
# i = 0
# while i < length1:
#     intake = int(input('Please enter a number: '))
#     mySet1.add(intake)
#     i += 1

# mySet2 = set(())
# length2 = int(input('Please enter a length for set 2: '))
# i = 0
# while i < length2:
#     intake = int(input('Please enter a number: '))
#     mySet2.add(intake)
#     i += 1

# newSet = mySet1.intersection(mySet2)
# print(newSet)

# Task 5

# words = ['boy', 'pen', 'girl', 'penis', 'physics', 'python', 'children', 'islam', 'pepper', 'tinubu', 'train']
# b = [x for x in words if len(x)%2 !=0]
# print(b)