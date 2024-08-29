def sum_all(*args):# multiple values
    print(args)
    for i in args:
        print(i * 2)# any name but use *, print(args) result tuple iterate
    return sum(args)

print(sum_all(1, 2))
"""print(sum_all(1, 2, 3, 4, 5))
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))"""