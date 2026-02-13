class User:
    age = 0;

    def __init__(self, name):
        print('я молодец!')
        self.username = name
        self.age = 0
    
    def sayName(self):
        print('меня зовут ', self.username)
    
    def sayAge(self):
        print(self.age)
    
    def setAge(self, newAge):
        self.age = newAge
