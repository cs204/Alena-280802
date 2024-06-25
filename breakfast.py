menu = {
   "кофе": 20.00,
   "чай": 10.00,
   "булочка": 5.00,
   "салат": 30.40,
   "пирожное": 45.50
}

s = 0

while True:
    try:
        d = input("Блюдо: ")
        if d in menu:
            s += menu[d]
        else:
            print(f"Извините, {d} нет в меню.")
    except EOFError:
        break
print()

print(f"Сумма: {s:.2f}")
