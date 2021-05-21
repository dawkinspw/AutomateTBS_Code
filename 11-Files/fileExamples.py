import os, shelve


testFile = open('testTex2.txt', 'a')
testFile.write('Testing abc\n')

shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['one', 'two', 'three']

print(shelfFile['cats'])
shelfFile.close()

# content = testFile.read()


# print(content)
# testFile.close()