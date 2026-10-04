s = input()
print(f"Длина: {len(s)}\n"
      f"Только буквы: {s.isalpha()}\n"
      f"Только цифры: {s.isdigit()}\n"
      f"Буквенно-цифровая: {s.isalnum()}\n"
      f"Содержит дефис: {"-" in s}")