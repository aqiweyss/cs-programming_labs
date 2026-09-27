distance, fuel, price = float(input()), float(input()), float(input())

quantity = (distance / 100) * fuel
cost = quantity * price

print(f"Топливо: {quantity:.2f} л\n"
      f"Стоимость: {cost:.2f} руб")
