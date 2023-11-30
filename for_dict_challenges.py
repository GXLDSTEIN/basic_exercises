# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {"first_name": "Вася"},
    {"first_name": "Петя"},
    {"first_name": "Маша"},
    {"first_name": "Маша"},
    {"first_name": "Петя"},
]


def unique_students(students: list[dict]) -> list[dict]:
    """
    returns list of dicts with unique students
    """
    unique_list = []
    for student in students:
        if student not in unique_list:
            unique_list.append(student)
    return unique_list


for student in unique_students(students):
    print(f'{student["first_name"]}: {students.count(student)}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторяющееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {"first_name": "Вася"},
    {"first_name": "Петя"},
    {"first_name": "Маша"},
    {"first_name": "Маша"},
    {"first_name": "Оля"},
]


def most_popular_name(students: list[dict]) -> str:
    n = 0
    for student in unique_students(students):
        if students.count(student) > n:
            n = students.count(student)
            name = student["first_name"]
    return name


print(f"Самое частое имя среди учеников: {most_popular_name(students)}")


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {"first_name": "Вася"},
        {"first_name": "Вася"},
    ],
    [  # это – второй класс
        {"first_name": "Маша"},
        {"first_name": "Маша"},
        {"first_name": "Оля"},
    ],
    [  # это – третий класс
        {"first_name": "Женя"},
        {"first_name": "Петя"},
        {"first_name": "Женя"},
        {"first_name": "Саша"},
    ],
]

for school_class in school_students:
    print(f"Самое частое имя среди учеников: {most_popular_name(school_class)}")


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [
    {"class": "2a", "students": [{"first_name": "Маша"}, {"first_name": "Оля"}]},
    {"class": "2б", "students": [{"first_name": "Олег"}, {"first_name": "Миша"}]},
    {
        "class": "2в",
        "students": [
            {"first_name": "Даша"},
            {"first_name": "Олег"},
            {"first_name": "Маша"},
        ],
    },
]
is_male = {
    "Олег": True,
    "Маша": False,
    "Оля": False,
    "Миша": True,
    "Даша": False,
}

# Задание 5
# По информации об учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {"class": "2a", "students": [{"first_name": "Маша"}, {"first_name": "Оля"}]},
    {"class": "3c", "students": [{"first_name": "Олег"}, {"first_name": "Миша"}]},
]
is_male = {
    "Маша": False,
    "Оля": False,
    "Олег": True,
    "Миша": True,
}
# ???
