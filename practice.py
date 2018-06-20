#FPS
#question 1

def f(n):
    num = 6 * n - 4
    return num

print (f(4))
print (f(5))
print (f(6))
print (f(7))

#question 2
 
def f(n):
    num = 1 / (3 ** n - 1)
    return num

print (f(1))
print (f(2))
print (f(3))
print (f(4))
print (f(5))

#question 3

def f(n):
    num = ( -1 ** n ) * ( 3 )
    return num

print (f(1))
print (f(2))
print (f(3))
print (f(4))
print (f(5))

#question 4

def f(n):
    num = 250 * 0.07 * n + 250
    return num

print(f(1))
print(f(3))
print(f(7))
print(f(20))

#question 5
def f(n):
    num = 325 * (1.04 ** n)
    return num

print(f(1))
print(f(3))
print(f(7))
print(f(20))

#FW
#question a

def m(h):
    amount = 1000 + 100 * h
    return amount

#question b

def b(m):
    bills = m / 20
    return bills

#question c

def b(h):
    amount = m(h)
    bills = m / 20
    return bills

#question d

def b(m):
    bills = m / 20
    return bills

print (m(5))

#question e

def m(h):
    return (h * 20) - 1000/100
print (m(100))
