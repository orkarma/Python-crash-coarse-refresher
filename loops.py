#LOOPS

#FOR LOOP
people = ['john','sara','tim','bob']
for person in people:
    print ('current person: ', person)

#ITERATE BY SEQ INDEX
for i in range(len(people)):
    print ('current person: ', people[i])
    
for i in range(0,10):
    print (i)

#WHILE loop
count = 0
while count <= 10:
    print('count: ', count)
    if count == 5:
        break
    count = count + 1