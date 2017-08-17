#CONDITIONALS

x = 4

#BASIC IF
if  x < 6:
    print ('this is true')

#ELSE IF
if x < 6:
    print ('this true')
else:
    print('this is false')

#ELIF
colour = 'red'

if colour == 'red':
    print ('colour is red')
elif colour == 'blue':
    print ('colour is blue')
else:
    print('colour is not red or blue')
   
#NESTED IF 
if colour == 'red':
    if x < 10:
        print ('colour is red and x is less than 10')
        
#LOGICAL OPERATORS        
if colour == 'red' and x < 10:
    print ('colour is red and x is less than 10')
    