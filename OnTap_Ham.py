def giaithua(n):
    gt=1
    for i in range (1,n+1):
        gt=gt*i
    return gt
gt_5=giaithua(5)

print ("5! =",gt_5)
def A(n,k):
    return giaithua(n)/giaithua(n-k)
def C(n,k):
    return giaithua (n)/(giaithua (n-k)*giaithua(k))

print ("Chinh hop chap 3 cua 5, A(5,3)=",A(5,3))