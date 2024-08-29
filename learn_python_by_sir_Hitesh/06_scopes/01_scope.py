username = "hira"

def func():
    username = "chai"
    print(username)

print(username)
func()

#func 2
x = 99 #global value
"""
def func2(y):
      z= x+y
      return z

result = func2(2)
print(result)"""

# not do this thing
"""def func3():
    global x
    x = 12

func3()
print(x)"""

def f1():
    x = 88
    def f2():
        print(x)
    return f2

myResult = f1()
myResult()

def chaiCoder(num):# closure /factory function
    def actual(x):
        return x ** num
    return actual

f = chaiCoder(2)
g = chaiCoder(3)

print(f(3))
print(g(3))

