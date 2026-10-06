start_temp = float(input())
end_temp = float(input())

if start_temp > end_temp:
    print("Охлаждение")
elif start_temp < end_temp:
    print("Нагрев")
else:
    print("Выключен")