train, city_dispatch, city_destination, time_dispatch, price = input().split(";", maxsplit=4)
print(f"Поезд: {train}\n"
      f"Маршрут: {city_dispatch} - {city_destination}\n"
      f"Отправление: {time_dispatch}\n"
      f"Цена: {(float(price)):.2f} руб")