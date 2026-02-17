from user import User
from card import Card

alex = User('Alex')

alex.sayName()
alex.setAge(33) #создали запрос на изменение возраста
alex.sayAge()

card = Card("1234 5678 8765 4321", "03/28", "Alex F")
card.pay(1000)