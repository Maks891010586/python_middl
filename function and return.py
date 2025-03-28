import time
import random


def generate_random_znak():
    znaks = ['*', '/', '+', '-']
    return random.choice(znaks)  # Более питонический способ выбора случайного элемента


def generate_random_number(from_number, to_number):
    if from_number < 0 or to_number < 0:
        return None
    if from_number > to_number:  # Добавлена проверка на корректность диапазона
        from_number, to_number = to_number, from_number
    return random.randint(from_number, to_number)


def calculate_expression(num1, znak, num2):
    if num1 is None or num2 is None:
        print('Ученики ещё не проходили отрицательные числа')
        return

    try:
        if znak == '+':
            result = num1 + num2
        elif znak == '-':
            result = num1 - num2
        elif znak == '*':
            result = num1 * num2
        elif znak == '/':
            if num2 == 0:  # Обработка деления на ноль
                print(f'{num1} {znak} {num2} = Ошибка: деление на ноль!')
                return
            result = num1 / num2
        else:
            print(f'Знак {znak} не поддерживается текущей версией программы')
            return

        # Форматирование вывода для деления (2 знака после запятой)
        if znak == '/':
            print(f'{num1} {znak} {num2} = {result:.2f}')
        else:
            print(f'{num1} {znak} {num2} = {result}')
    except Exception as e:
        print(f'Ошибка при вычислении: {e}')


def do_lesson_stage(text_to_print, time_to_sleep=1):
    print(text_to_print)
    time.sleep(time_to_sleep)


def main():
    # Урок начинается
    do_lesson_stage('1. Урок МАТЕМАТИКИ начался')

    # Вовочка решает пример
    do_lesson_stage('2. Вовочка начал решать пример')
    calculate_expression(
        generate_random_number(1, 50),
        generate_random_znak(),
        generate_random_number(1, 50)
    )

    # Маша решает пример
    do_lesson_stage('8. Маша начала решать пример')
    calculate_expression(
        generate_random_number(1, 100),
        generate_random_znak(),
        generate_random_number(10, 100)
    )

    # Урок заканчивается
    do_lesson_stage('10. Урок закончился')


if __name__ == "__main__":
    main()