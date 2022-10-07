import csv
import sys
from io import StringIO


'''
Ввод:
from,to
1,2
1,3
2,4
'''


# Функция для считывания данных из входного потока
def read_csv():
    # Считываем все линии входного потока до закрывающего ^D (Ctrl + D)
    csv_content = sys.stdin.readlines()
    # Десериализируем входные данные
    reader = csv.reader(csv_content)
    # Убираем строку хедеров
    next(reader)
    # Преобразуем перечислимый тип в список
    data = list(reader)
    # Возвращаем полученный список связей
    return data


# Функция для классификации отношений между элементами
def classify(cons: list):
    # Создаем пустые списки для каждого типа отношений
    t1 = list()
    t2 = list()
    t3 = list()
    t4 = list()
    t5 = list()

    # Идем в цикле по всем данным связям. Пусть con - первая связь
    for con in cons:
        # Добавляем первую связь в список 1го типа отношений
        t1.append(con)
        # Добавляем первую связь, но в обратном порядке, в список 2го типа отношений
        t2.append(con[::-1])

        # Идем в цикле по всем данным связям, кроме текущей. Пусть other_con - вторая связь
        for other_con in [c for c in cons if c != con]:
            # Если совпадает конец первой и начало второй связей
            if con[1] == other_con[0]:
                # Добавляем связь из начала первой связи в конец второй связи в список 3го типа отношений
                t3.append([con[0], other_con[1]])
                # Добавляем связь из конца первой связи в начала второй связи в список 4го типа отношений
                t4.append([other_con[1], con[0]])
            # Если совпадают начала первой и второй связей
            elif con[0] == other_con[0]:
                # Добавляем связь из конца первой в конец второй связи в список 5го типа отношений
                t5.append([con[1], other_con[1]])

    # Возвращаем списки всех типов отношений
    return t1, t2, t3, t4, t5


# Функция, заданная по условию в Canvas
def task(csv_str: str):
    csv_io = StringIO(csv_str)
    reader = csv.reader(csv_io)
    data = list(reader)
    type_1, type_2, type_3, type_4, type_5 = classify(data)
    return [
        sorted(set(node[0] for node in type_1)),
        sorted(set(node[0] for node in type_2)),
        sorted(set(node[0] for node in type_3)),
        sorted(set(node[0] for node in type_4)),
        sorted(set(node[0] for node in type_5))
    ]


# Функция, которая была написана на паре
def main():
    # Считываем входные данные, занося их в список связей
    connections = read_csv()
    # Классифицируем по списку связей, получая 5 списков - для каждого типа отношений
    type_1, type_2, type_3, type_4, type_5 = classify(connections)
    # Выводим содержимое списков
    print(f"""\
    Тип 1: {type_1}
    Тип 2: {type_2}
    Тип 3: {type_3}
    Тип 4: {type_4}
    Тип 5: {type_5}\
    """)


if __name__ == "__main__":
    print(task("1,2\n1,3\n2,4"))
    print(task("1,2\n1,3\n3,4\n3,5"))
