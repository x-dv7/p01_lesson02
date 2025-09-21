
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

        if self.val4 % 2 == 0 and self.val4 % 3 == 0:
            print('делится на 2 и на 3')
        elif self.val4 % 2 == 0:
            print('делится на 2')
        elif self.val4 % 3 == 0:
            print('делится на 3')
        
    def exersice5(self):
        """Метод задания 5."""
        self.val5 = int(input('Введите число: '))
        if self.val5 is None:
            print('None')
        elif 10 <= self.val5 <= 20: 
            print('[10, 20]') 

    def exersice6(self):
        """Метод задания 6."""
        self.val6 = input('Введите команду: ')
        match self.val6:
            case 'start':
                print('Запуск')
            case 'stop':
                print('Остановка')
            case 'pause':
                print('Пауза')
            case _:
                print('Неизвестная команда')
    
    def exersice7(self):
        """Метод задания 7."""
        for i in range(1, 6, 1):
            print(i ** 2)
        lv_p = str()
        while lv_p != '1234':
            lv_p = input('Введите пароль: ')
        else:
            print('Успешный вход')

    def excersice8(self):
        """Метод задания 8."""
        pass


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
        case 5:
            lo_ex.exersice5()
        case 6:
            lo_ex.exersice6()
        case 7: 
            lo_ex.exersice7()
        case 8:
            lo_ex.excersice8()
        case _:
            print('Такого задания нет')




if __name__ == '__main__':
    main()
