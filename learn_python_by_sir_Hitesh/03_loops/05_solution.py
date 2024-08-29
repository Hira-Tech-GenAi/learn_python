input_string = "teether"

for char in input_string:
    print(char)
    if input_string.count(char)== 1:
        print("Char is :", char)
        break