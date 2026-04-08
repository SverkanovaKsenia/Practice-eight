students = {
    "Иванов": {"английский", "китайский"},
    "Воробьев": {"английский", "немецкий"},
    "Брагин": {"французский", "китайский"},
    "Суслов": {"испанский"},
    "Громов": {"китайский", "японский"}
}

all_languages = set()

for langs in students.values():
    all_languages.update(langs)

print("Количество разных языков:", len(all_languages))
print("Все языки:", sorted(all_languages))

chinese_students = []

for student, langs in students.items():
    if "китайский" in langs:
        chinese_students.append(student)

print("Студенты, знающие китайский:", chinese_students)