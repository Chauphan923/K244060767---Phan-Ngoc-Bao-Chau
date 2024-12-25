def seperate(n):
    n1=n//100
    n2=(n//10)%10
    n3=(n%100)%10
    return n1,n2,n3
n=587
n1,n2,n3=seperate(n)
print(f"n={n}, co cac chu so:")
print("n1=",n1)
print("n2=",n2)
print("n3=",n3)