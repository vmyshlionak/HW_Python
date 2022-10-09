class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def  walk(self):
        return "I can walk!"

    def work(self):
        return "I am working"

employee_1 = Employee('Maria','Sukhova')

print(employee_1.name)
print(employee_1.surname)

class Developer(Employee): #подкласс наследует методы родительского класса
    def __init__(self, name, surname, language):
        super().__init__(name, surname)
        self.__language = language

    def coding(self):
        return "I am coding"

    def work(self):
        return 'I am coder'

    def get_language(self):
        return "My language is " + f'{self.__language}'

    def set_language(self, new_language):
        self.__language = new_language

dev1 = Developer("Ivan", "Ivanov", "Python")
print(dev1.walk())
print(dev1.surname)

# dev1.__language = "Java"
# print(dev1.__language) # выдаст ошибку, что нет такого атрибута, потому что он приватный!!! с двумя __
print(dev1.get_language())

dev1.set_language("Java") # способ изменения приватных атрибутов через метод!!!
print(dev1.get_language())
print(dev1.__dict__) # просмотр всех имен и значений атрибутов экземпляра класса в виде словаря
# print(issubclass(Developer, Employee))
# print(type(dev1))
# print(dev1.work())