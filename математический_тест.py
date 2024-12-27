# это добавление библиотеки
import random
# создание функции с именем(ganerete math question)и двыумя параметрами (a, b)
def generate_math_question(a, b):
    num1 = random.randint(a, b)
    num2 = random.randint(a, b)
    operator = random.choice(["+", "-", "*", "/" ])
    question = f"{num1} {operator} {num2}"
    return question


# Проверка ответа пользователя на правильность
def check_answer(a2, b3):
    try:
        eval1 = eval(a2)
        eval2 = eval(b3)
        if eval1 == eval2:
            return True
        else:
            return False
    except ValueError:
        return False
    except NameError:
        return  False

def math_quiz(number_of_questions = 5):
    print("Добро пожаловать в mатематический тест!")
    correct_answers = 0

    for i in range(number_of_questions):
        question = generate_math_question(1, 10)
        answer = input(f"{question} = ")
        if check_answer(question, answer):
            correct_answers += 1


    print("Тест завершен.")
    print(f"Вы правильно решили {correct_answers} из {number_of_questions} вопросов.")

    if correct_answers * 100 / number_of_questions > 80:
        print("Отлично! Вы получаете оценку A.")
    elif correct_answers * 100 / number_of_questions > 60:
        print("Хорошо! Вы получаете оценку B.")
    else:
        print("Попробуйте еще раз. Вы получаете оценку C.")


# Запуск теста
math_quiz(int(input("Введите количество заданий которое вы хотите: ")))
input("нажмите Enter для выхода:")