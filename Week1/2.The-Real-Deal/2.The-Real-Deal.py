# Task: Sum Numbers in Matrix

def sum_matrix(m):

    sum_matrix = 0
    try:
        for row in m:
            for col in row:
                sum_matrix = sum_matrix + col
        return (sum_matrix)
    except IndexError:
        row = 'null'


print (sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print (sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print (sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))
print (sum_matrix([[1, 2, 10, 22], [3, 4], [5, 6, 17], [7, 8, 1, 3, 5], [9, 10, 11 ,19, 20]]))


# Task: Zero Insertion
def zero_insert(n):

    if n<0:
        print ("n must bigger than 0!")
        return
    if n>=0 and n<=9:
        for number in range(0, 10):
            if n == number:
                return number

    num_len = int(len(str(n)))
    num_list = []

    for nums in range(0, num_len):

        result = n % 10
        n = n // 10
        num_list.append(result)
    num_list.reverse()

    try:
        for num in range(0, len(num_list)*2):

            if num_list[num] == num_list[num+1] or (num_list[num] + num_list[num+1]) % 10 == 0:
                num_list.insert(num+1, 0)

    except IndexError:
        num = 'null'

    string = ""
    for numb in range(0, len(num_list)):

        string = string + str(num_list[numb])

    number = int(string)
    return (number)

print (zero_insert(116457))
print (zero_insert(55555555))
print (zero_insert(1))
print (zero_insert(6446))
print (zero_insert(114673918299))


# Task: Counting substrings

def count_substrings(haystack, needle):

    return haystack.count(needle)


print (count_substrings("This is a test string", "is"))
print (count_substrings("babababa", "baba"))
print (count_substrings("Python is an awesome language to program in!", "o"))
print (count_substrings("We have nothing in common!", "really?"))
print (count_substrings("This is this and that is this", "this"))


# Task: Is number balanced?
def is_number_balanced(n):
    if n<0:
        print ("n must bigger than 0!")
        return
    if n>=0 and n<=9:
        return True
    count = 0
    num_len = int(len(str(n)))
    num_list = []

    for elem in range(0, num_len):

        result = n % 10
        n = n // 10
        num_list.append(result)
        count+=1
    num_list.reverse()

    if count % 2 != 0: # броят на цифрите в числото не е четен

        a = sum(int(i) for i in num_list[:len(num_list)//2])
        b = sum(int(s) for s in num_list[len(num_list)//2+1:])
        if(a == b):
            return True
        else:
            return False

    if count % 2 == 0: # броят на цифрите в числото  е четен

        p = sum(int(y) for y in num_list[:count//2])
        q = sum(int(z) for z in num_list[count//2:])

        if p == q:
            return True
        else:
            return False

print (is_number_balanced(1035104))
print (is_number_balanced(3856987))
print (is_number_balanced(1035022))
print (is_number_balanced(3958980))
print (is_number_balanced(9))
print (is_number_balanced(11))
print (is_number_balanced(13))
print (is_number_balanced(121))
print (is_number_balanced(4518))
print (is_number_balanced(28471))
print (is_number_balanced(1238033))


# Task: Number containing all digits?

def contains_digits(number, digits):

    num_len = int(len(str(number)))
    number_list = []

    for nums in range(0, num_len):

            result = number % 10
            number = number // 10
            number_list.append(result)

    if set(digits).issubset(set(number_list)):
            return True
    else:
            return False

print (contains_digits(402123, [0, 3, 4]))
print (contains_digits(666, [6,4]))
print (contains_digits(123456789, [1,2,3,0]))
print (contains_digits(456, []))
print (contains_digits(7464383000302, [4,7,6]))


# Task: Number containing a single digit?

def contains_digit(number, digit):

    number_length = int(len(str(number)))

    for num_len in range(0, number_length):

        result = number % 10
        number = int(number/10)

        if(result == digit):
            return True
    return False


def main():
        print (contains_digit(12345, 5))
        print (contains_digit(123, 4))
        print (contains_digit(42, 2))
        print (contains_digit(1000, 0))
        print (contains_digit(12346789, 5))
        print (contains_digit(1234678932, 0))




if __name__ == "__main__":
    main()



# Task: Check if a number has a prime number of divisors

import math

def prime_number_of_divisors(n):
    if(n<0):
        n = abs(n)
    div = 1
    for divisor in range(2,n+1):
        if(n % divisor == 0 or (n % divisor == 0 and n == divisor)):
            div = div + 1

    divider = 2
    maxDivider = math.sqrt(abs(div))
    if div == 2 or div == 3:
        return True
    while divider <= maxDivider:
        if(div % divider == 0):
            return False
        divider+=1
    return True


def main():
    print (prime_number_of_divisors(8))
    print (prime_number_of_divisors(7))
    print (prime_number_of_divisors(9))
    print (prime_number_of_divisors(35))
    print (prime_number_of_divisors(-27))
    print (prime_number_of_divisors(-625))



if __name__ == "__main__":
    main()

# Task: Check if integer is prime

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

def main():
    print (is_prime(-42))
    print (is_prime(255))
    print (is_prime(37))
    print (is_prime(1))
    print (is_prime(2))
    print (is_prime(8))
    print (is_prime(11))
    print (is_prime(-10))


if __name__ == "__main__":
    main()

# Task: Sum all divisors of an integer

def sum_of_divisors(n):
    sum=1

    for divisor in range(2,n+1):

        if(n % divisor == 0 or (n % divisor == 0 and n == divisor)):
            sum = sum + divisor

    return sum

    return sum

def main():
    print (sum_of_divisors(15))
    print (sum_of_divisors(8))
    print (sum_of_divisors(7))
    print (sum_of_divisors(1))
    print (sum_of_divisors(1000))

    if __name__ == "__main__":
        main()

