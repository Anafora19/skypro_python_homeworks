class User:
    def __init__(self, first_name, last_name): #конструктор
        self.first_name = first_name
        self.last_name = last_name

    def say_first_name(self): # тело метода Имя
        print("Имя: ", self.first_name)

    def say_last_name(self): #тело метода Фамилия
        print("Фамилия: ", self.last_name)

    def say_full_name(self): #тело метода Имя и Фамилия
        print("Имя и Фамилия: ", self.first_name, self.last_name)

