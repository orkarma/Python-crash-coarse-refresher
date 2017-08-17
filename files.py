#open a file
fo = open('test.txt', 'w')
#get some info 
print('Name: ', fo.name)
print('is closed: ', fo.closed)
print('opening mode: ', fo.mode)
#write to file
fo.write('i love python')
fo.write(' and javascript.')
#close file
fo.close
#open to append
fo = open('test.txt', 'a')
fo.write(' i also like PHP.')
fo.close
#read from file
fo = open('test.txt', 'r+')
text = fo.read()
print(text)
#create file
fo = open('test2.txt', 'w+')
fo.write('this is my new file')
fo.close