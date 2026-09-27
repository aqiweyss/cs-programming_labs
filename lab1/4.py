duration_trip = int(input())

hours = str(duration_trip // 3600)
minutes = str((duration_trip % 3600) // 60)
seconds = str((duration_trip % 3600) % 60)

print(f"{hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}")