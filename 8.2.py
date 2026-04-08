scores = {
    1: "АВЕИНОРСТ",
    2: "ДКЛМПУ",
    3: "БГЁЬЯ",
    4: "ЙЫ",
    5: "ЖЗХЦЧ",
    8: "ШЭЮ",
    10: "ФЩЪ"
}
word = input("Введите слово: ").upper()
total = 0
for letter in word:
    for score, letters in scores.items():
        if letter in letters:
            total += score

print("Стоимость слова:", total)
