countries = {
    "Россия": "Москва",
    "Франция": "Париж",
    "Германия": "Берлин",
    "Италия": "Рим",
    "Испания": "Мадрид"
}

print("Все страны и столицы:")
for country, capital in countries.items():
    print(country, "-", capital)

user_country = input("Введите страну: ")

if user_country in countries:
    print("Столица:", countries[user_country])
else:
    print("Такой страны нет в словаре")

print("Отсортированный список:")
for country in sorted(countries):
    print(country, "-", countries[country])