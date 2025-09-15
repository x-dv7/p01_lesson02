
"""Основной модуль приложения lesson02."""

def todo():
    """Функция todo."""
    pass

def done():
    """Функция done."""
    print('Готово!')

class ClassWithTodo:
    """Класс ClassWithTodo."""
    def todo(self):
        """Метод todo."""
        ...
    
    def done(self):
        """Метод done."""
        print('Готово!')

class ClassExercise:
    """Класс ClassExercise."""
    def name_and_age(self):
        """Метод задания 2."""
        # Ввод имени
        self.name = input('Введите имя: ')
        # Ввод возраста
        self.age = int(input('Введите возраст: '))
        # Вывод имени и возраста
        print('Привет, <' + self.name + '>! Через 5 лет тебе будет <' + str(self.age + 5) + '> ') 

    def exersice3(self):
        """Метод задания 3."""
        if True:
            print('Поставил 4 пробела внутри блока if')

    def exersice4(self):
        """Метод задания 4."""
        self.val4 = int(input('Введите число: '))
        if self.val4 > 0:
            print('positive')
        elif self.val4 == 0:
            print('zero')
        else:
            print('negative')

def main():
    """Главная функция приложения lesson02.
    
    Выводит пример задания, печатает сообщение 'Задания из lesson02'
    и спрашивает пользователю ввести номер задания.
    Если задание существует, то вызывает соответствующий метод класса ClassExercise.
    Если задание не существует, то печатает сообщение 'Такого задания нет'.
    """
    lo_ex = ClassExercise()
    print('Задания из lesson02')
    ex = int(input('Введите номер задания: '))
    match ex:
        case 2:
            lo_ex.name_and_age()
        case 3:
            lo_ex.exersice3()    
        case 4:
            lo_ex.exersice4()
        case _:
            print('Такого задания нет')




if __name__ == '__main__':
    main()
