from address import Address
from mailing import Mailing

to_address = Address('127000', 'Москва', 'Академика Королёва', '12', '45')
from_address = Address('633009', 'Бердск', 'Рогачева', '1', '152')
cost = 870
track = ('640370457')

mailing = Mailing(to_address, from_address, cost, track)

print(f'Отправление: {track}, из {from_address} \
в {to_address}. Стоимость: {cost} рублей.')
n