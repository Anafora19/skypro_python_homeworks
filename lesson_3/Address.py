class Address: #создание класса адрес

    def __init__ (self, index, city, street, home, room): #конструктор с параметрами
        self.index = index
        self.city = city
        self.street = street
        self.home = home
        self.room = room