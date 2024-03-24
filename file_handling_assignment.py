try:
    with open('my_file.txt', 'w') as fileA:
        num = 34293
        fileA.write(f"I love my wife \n{num} \nI love Nimat")
    with open('my_file.txt', 'r') as fileA:
        print(fileA.read())
except (FileNotFoundError, PermissionError):
    print('Check the name of file')
else:
    print('Continue with the file work, it has been opened and read')
finally:
    print('Move on to unlock week 6')

    
    
 
