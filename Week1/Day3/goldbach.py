import copy
import math

def is_prime(n):
    divider = 2
    maxDivider = math.sqrt(abs(n))
    if(n == 1):
        return False
    while divider <= maxDivider:
        if(n % divider == 0):
            return False
        divider+=1
    return True

def goldbach(n):
    if n < 4 or n % 2 != 0:
        raise Exception("Please enter a even integer bigger than 2!")

    goldbach_list = []
    noprimes = [j for i in range(2, 8) for j in range(i*2, n, i)]
    primes = [x for x in range(2, n) if x not in noprimes and is_prime(x)]
    primes_copy = copy.deepcopy(primes)

    for nums in primes:
        while len(primes_copy) != 0:
            element = primes_copy.pop(0)
            if nums + element == n:
                if (element, nums)  in goldbach_list:
                    continue
                goldbach_list.append((nums, element))
        primes_copy = copy.deepcopy(primes)
    return goldbach_list

def main():
    # Enter values: 4, 6, 8, 10, 100, 150 , 250 ...
    number = int(input("Enter a even integer bigger than 2: "))
    print(goldbach(number))

if __name__ == "__main__":
    main()
