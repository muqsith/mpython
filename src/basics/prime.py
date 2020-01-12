def primes(n):
    """Prints a statement about a number whether it is prime or not, 
        for all the numbers in the range of 2 to n"""
    if n <= 0:
        print('Please provide numbers greater than 0')
    elif n > 0 and n < 2:
        print(n, 'is not a prime number')
    elif n == 2:
        print("2 is a prime number")
    else:

        for i in range(2, n+1):
            for j in range(2, i):
                if i % j == 0:
                    print(i, 'equals', j , '*', i//j)
                    break
            else: 
                print(i, 'is a prime number')
        


n = int(input("Enter the limit for prime numbers\n"))
primes(n)