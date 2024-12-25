def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

print ("5!=", factorial (6))

def H10ToH2(n):
    if n>0:
        sd=n%2
        n=n//2
        H10ToH2(n)
        print(sd,end=" ")

n=587
H10ToH2(n)