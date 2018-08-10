def sumOfAP( n,a,d) :
    sum = 0
    i = 0
    while i < n :
        sum = sum + a
        a = a + d
        i = i + 1
    return sum
     
n,a,d=map(int,raw_input().split())
print (sumOfAP(n,a,d))
 
