#FUNTIONS

#CREATE A FUNTION

def sayHello(name = 'John'):
    print('hello', name)
    
sayHello('Brad')

#RETURN A Value

def getSum (num1, num2):
    total = num1 + num2
    return total

numSum = getSum(1,2)
print(numSum)

def addOneToNum(num):
    num = num + 1
    print('value inside funtion: ', num)
    return

num = 5
addOneToNum(num)
print('value outside funtion: ', num)

def addOneToList(myList):
    myList.append(4)
    print('value inside funtion: ', myList)
    return

myList = [1,2,3]
addOneToList(myList)
print('value outside funtion: ', myList)