distance = 25
if distance < 3:
    transport = "walk"
elif distance <= 15:
    transport = "bike"
else:
    transport = "car"

print("transport is ", transport )