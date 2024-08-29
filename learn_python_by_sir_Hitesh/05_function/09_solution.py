def even_generator(limit):# yield return and function kitna kam kr chuka he
    
    for i in range(2, limit + 1, 2):
        yield i

for num in even_generator(10):
    print(num)

