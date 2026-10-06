ceil = float(input())
age = int(input())

if age > 120 or age < 0 or ceil < 0:
    print("Ошибка")

elif 0 <= age <= 5:
    print(f"Стоимость: {int(ceil * 0):.2f}")

elif 6 <= age <= 17:
    print(f"Стоимость: {int((ceil / 100) * 50):.2f}")

elif 18 <= age <= 59:
    print(f"Стоимость {int(ceil):.2f}")

elif 60 <= age <= 120:
    print(f"Стоимость {int((ceil/100) * 70):.2f}")