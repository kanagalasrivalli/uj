def sumOfAP( n,d,a) :
    sum = 0
    i = 0
    while i < n :
        sum = sum + a
        a = a + d
        i = i + 1
    return sum
     
n,d,a=map(int,raw_input().split())
print (sumOfAP(n,d,a))
 
