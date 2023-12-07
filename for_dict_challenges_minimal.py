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
    reveal_type(
        school_class
    )  # Revealed type is "builtins.list[builtins.dict[builtins.str, builtins.str]]"

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


for school_class in school:
    reveal_type(
        school_class
    )  # Revealed type is "builtins.list[builtins.dict[builtins.str, builtins.str]]"
    reveal_type(
        school
    )  # Revealed type is "builtins.list[builtins.dict[builtins.str, typing.Sequence[typing.Collection[builtins.str]]]]"
    print(type(school_class))  # <class 'dict'>
    print(type(school))  # <class 'list'>
