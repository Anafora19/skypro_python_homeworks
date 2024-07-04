from Address import Address
from Mailing import Mailing

#данные для класса "Адрес"

to_address = Address("123456", "Moscow", "Lenin Street", "10", "5") #адрес отправки
from_address = Address("654321", "Saint Petersburg", "Pushkin Street", "20", "10") #адрес доставки
cost = 1000 #стоимость
track = "1114445577" #трек-номер

#данные для класса "Почтовое отправление"

package = Mailing(to_address, from_address, cost, track) #создание посылки
to_address_info = f"{to_address.index}, {to_address.city}, {to_address.street}, {to_address.home} - {to_address.room}" #даные для отправления
from_address_info = f"{from_address.index}, {from_address.city}, {from_address.street}, {from_address.home} - {from_address.room}"#данные для получения

#Вывод

print(f"Отправление {track} из {to_address_info} в {from_address_info}. Стоимость {cost} рублей.")