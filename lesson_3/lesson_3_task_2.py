from smartphone import Smartphone

catalog = ([]) #Объявили переменную, которая хранит список

phone1 = Smartphone("Apple", "iPhone X", "+79123456789") #элементы списка
phone2 = Smartphone("Samsung", "Galaxy S10", "+79234567890")
phone3 = Smartphone("Google", "Pixel 4", "+79345678901")
phone4 = Smartphone("OnePlus", "7 Pro", "+79456789012")
phone5 = Smartphone("Huawei", "P30 Pro", "+79567890123")

catalog.append(phone1) #добавление элемента в список
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog: #цикл печати каталога
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}") 