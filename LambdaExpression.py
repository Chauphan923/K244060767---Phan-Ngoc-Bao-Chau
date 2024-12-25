def handle(f,x):
    return f(x)
#cach 1: thu ra lenh cho lambda lam ham tinh kiem tra so le
ret1 =  handle(lambda x:x%2!=0,7) # ham nac danh
print (ret1)
#cach 2: viet tuong minh ra (ten ham ro rang ra) kiem tra so le

def isOdd(n):
    return n%2!=0
ret2=handle(lambda x:isOdd(x),7)
ret3=handle(isOdd,7)
print ("ret2=",ret2)
print ("ret3=",ret3)

def factorial (n):
    fact=1
    for i in range (1,1+n):
        fact=fact*i
    return fact
ret4=handle(lambda x:factorial(x),5)
print("5!=",ret4)

def handle2(f,x,y):
    return (f(x,y))
ret5=handle2(lambda x,y: x+y, 5, 3)
print(ret5)