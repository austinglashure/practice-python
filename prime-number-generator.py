primes = [2]

num = int(input("Please specify upper bound: "))

for i in range(2, num + 1):
    
    isPrime = True
    
    for prime in primes:
    
        if i == prime:
            isPrime = False
            break
        
        elif i % prime == 0:
            isPrime = False
        
    if isPrime:
        primes.append(i)

print("Your prime numbers between 1 and {}".format(num))
for number in primes:
    print(number)
        
