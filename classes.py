#classes & objects

class Person:
    __name = ''
    __email = ''
    
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
    
    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def set_email(self, email):
        self.__email = email
        
    def get_email(self):
        return self.__email
    
    def toString(self):
        return '{} can be contacted at {}'.format(self.__name, self.__email)
        
#brad = Person('Brad Smith', 'Brad.s@hotmail.com')
#brad.set_name('Brad Smith')
#brad.set_email('brad.s@hotmail.com')
#print(brad.toString())

class Customer(Person):
    
    __balance = 0
    
    def __init__(self, name, email, balance):
        self.__name = name
        self.__email = email
        self.__balance = balance
        super(Customer, self).__init__(name, email)
    
    def set_balance(self, balance):
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
    
    def toString(self):
        return '{} has a balance of {} and can be contacted at {}'.format(self.__name, self.__balance, self.__email)
    
john = Customer('John Doe', 'jdoe@gmail.com', 100)

print(john.toString())

john.set_balance(493)

print(john.toString())