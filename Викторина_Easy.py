import tkinter as tk
import sys

root = tk.Tk()
root.title('Викторина')
root.geometry('900x200+250+150')

questions = [
    '1.Что делает команда input?',
    '2.Какой параметр нужно использовать, чтобы поставить * между словами?',
    '3.Какой параметр нужно использовать чтобы поставить # в конце строки?',
    '4.Что означает оператор **?',
    '5.Что означает оператор %?',
    '6.Что означает //?',
    '7.В Python проверка условия осуществляется при помощи какого условного оператора?',
    '8.Что такое блок кода?',
    '9.Что делает условный оператор == ?',
    '10.Для чего нужен каскадный оператор?',
    '11.Какая функция округляет число x до ближайшего целого?',
    '12.Какая функция округляет число x вниз («пол»)?',
    '13.Какая функция округляет число x вверх («потолок»)?',
    '14.Что делает функция pow (x, n)?',
    '15.Для чего нужен модуль math?',
]

options = [
    ['Команда input() считывает введенные с клавиатуры данные',
     'Команда input() используется чтобы посчитать длину строки', 'Команда input() используется для вывода значений'],
    ['end', 'sep', 'float'],
    ['end', 'sep', 'float'],
    ['Возведение в степень', 'Чтобы посчитать длину строки', 'Целочисленное деление'],
    ['Остаток от деления', 'Преобразует угол x, заданный в градусах, в радианы', 'Целочисленное деление'],
    ['Возведение в степень', 'Остаток от деления', 'Целочисленное деление'],
    ['for', 'if - else', 'while'],
    ['Блоком кода называют набор комментариев, которые не влияют на работу программы',
     'Блоком кода называют специальный элемент программы, который служит для хранения данных, но не выполняет никаких действий',
     'Блоком кода называют объединённые друг с другом строки'],
    ['Он сравнивает типы данных, а не значения переменных', 'Он проверяет два элемента на равенство',
     'Он выполняет присваивание значения переменной, а не сравнение двух значений'],
    ['Если требуется проверить несколько условий',
     'Если требуется увеличить скорость выполнения программы',
     'Если требуется обнаружить и исправить ошибку в коде'],
    ['floor(x)', 'int(x)', 'round(x)'],
    ['floor(x)', 'ceil(x)', 'round(x)'],
    ['abs(x)', 'round(x)', 'ceil(x)'],
    ['Вычисляет квадрат числа x', 'Вычисляет сумму числа x и степени n', 'Возводит числа x в степень n'],
    ['Используется для анализа и обработки изображений', 'Используется для решения уравнений и систем уравнений',
     'Этот модуль предоставляет обширный функционал для проведения вычислений с вещественными числами'],
]

correct_answers = [
    0, 1, 0, 0, 0, 2, 1, 2, 1, 0, 2, 2, 0, 2, 2
]

score = 0
question_number = 0

question_label = tk.Label(root, text=questions[question_number])
question_label.pack()

answer_buttons = []


def set_answers():
    for i in range(len(options[0])):
        answer_button = tk.Button(root, text=options[question_number][i],
                                  command=lambda i=i: check_answer(i))
        answer_button.pack()
        answer_buttons.append(answer_button)
set_answers()

result_label = tk.Label(root, text='')
result_label.pack()

grade_label = tk.Label(root, text='')
grade_label.pack()


def check_answer(user_answer):
    global question_number, score
    if user_answer == correct_answers[question_number]:
        score += 1
    question_number += 1

    if question_number < len(questions):
        question_label.config(text=questions[question_number])
        for i in range(len(answer_buttons)):
            answer_buttons[i].config(text=options[question_number][i])
    else:
        result_label.config(text=f'Ваш результат: {score}/{len(questions)}')
        calculate_grade()


def calculate_grade():
    global score
    if score < 7:
        grade = '2'
    elif 7 <= score <= 10:
        grade = '3'
    elif 10 <= score <= 13:
        grade = '4'
    else:
        grade = '5'
    grade_label.config(text=f'Твоя оценка: {grade}')
    
def exit_quiz():
    root.destroy()
    sys.exit()


exit_button = tk.Button(root, text='Выход', command=exit_quiz)
exit_button.pack()


root.mainloop()
