import math
def  findPrimeFactors(num):
    #prime factors: 2,3,5,7...

    #if the number is even then its divissble by 2 
    res = []
    while num % 2 == 0:
        res.append(2)
        num /= 2

    # number will  be odd now
    # 15 ==> 3,5 (3, )
    #75 ==> 5,15,3,5
    #16 ==. [ 1,2,3,4   ,5,6,7,8,9,10,11,12,13,14,15,16]
    sqrt = int(math.sqrt(num))+1

    for i in range(3,sqrt,2):
        while num%i == 0:
            res.append(i)
            num /= i
    
    if num > 2:
        res.append(num)
    return res

print(findPrimeFactors(100))
        
            
        

    