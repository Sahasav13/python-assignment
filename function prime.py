def check_prime(num):
    if num==0 or num==1:
        return "not a prime"
    elif num>1:
     for i in range(2,num):
         if (num%i)==0:
             return "not a prime"
         else :
            return "prime"
        
print(check_prime(5))
