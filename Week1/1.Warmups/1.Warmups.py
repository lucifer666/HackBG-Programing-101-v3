# Task: Char Histogram

def char_histrogram(string):
    dict = {}

    for elem in range(0, len(string)):

        count_chars = string.count(string[elem]) # броя всеки char на стринга, колко пъти се повтаря
        if string[elem] not in dict: # ако даден елемент от стринга не се съдържа в речника
            dict[string[elem]] = count_chars # се добавя string[elem] и се добавя неговия ключ count_chars
    return dict


print (char_histrogram("Python!"))
print (char_histrogram("AAAAaaaa!!!"))
print (char_histrogram("HehllLLoWwWw00rLd1!...!"))


# Task: Hack Numbers

def is_hack(n):
     binary = bin(n)[2:]
     string = str(binary)
     bin_list = []
     count = 0
     for nums in range(0, len(string)):

          reverse = binary[::-1]
          bin_list.append(binary[nums])
     is_palindrome = False
     if binary == reverse:
        is_palindrome = True
     for numbers in range(0, len(bin_list)):

          if int(bin_list[numbers]) == 1:
              count += 1

     return is_palindrome and count % 2 != 0

def next_hack(n):
    while True:
        if is_hack(n):
            return n
        n += 1


print (next_hack(0))
print (next_hack(10))
print (next_hack(8031))

# Task: Palindrome Score

def p_score(n):

    string = str(n)
    reverse = ""
    for char in range(0, len(string)):

        reverse += string[(len(string)-1) - char]

    rev_number = int(reverse)


    if rev_number == n:
        p = 1
        return p
    else:
        p = 2
        p_s = n + rev_number
        while p_s != (int(str(p_s)[::-1])):
            var = p_s
            p_s = var + int(str(var)[::-1])
            p+=1
        return (p)

def main():
    print (p_score(121))
    print (p_score(48))
    print (p_score(198))
    print (p_score(1))
    print (p_score(147))


if __name__ == "__main__":
    main()



# Task: Fibonacci number

def fib_number(n):

    var = 0
    var_1 = 1
    fib_list = [1]

    try:
        for numbers in range(2, n+1):

           fib = var
           var = var_1
           var_1 = fib + var
           fib_list.append(var_1)

        string = "".join(map(str, fib_list))
        number = int(string)
        return (number)


    except IndexError:
        numbers = 'null'

def main():
    print (fib_number(3))
    print (fib_number(10))
    print (fib_number(5))
    print (fib_number(2))


if __name__ == "__main__":
    main()


# Task: First nth members of Fibonacci

def fibonacci(n):

    var = 0
    var_1 = 1
    fib_list = [1]

    try:
        for numbers in range(2, n+1):

           fib = var
           var = var_1
           var_1 = fib + var
           fib_list.append(var_1)
        print (fib_list)

    except IndexError:
        numbers = 'null'

def main():
    print (fibonacci(1))
    print (fibonacci(2))
    print (fibonacci(3))
    print (fibonacci(10))
    print (fibonacci(100))


if __name__ == "__main__":
    main()


# Task: Palindrome

def palindrome(obj):

    string = str(obj)
    reverse = ""
    for char in range(0, len(string)):

        reverse += string[(len(string)-1) - char]
    if reverse == string:
        return True
    else:
        return False


def main():
    print (palindrome(121))
    print (palindrome("kapak"))
    print (palindrome("baba"))
    print (palindrome("nemogaagomen"))


if __name__ == "__main__":
    main()


# Task: Descreasing sequence?

def is_decreasing(seq):

    count = 0
    try:
        for element in range(0, len(seq)):

            if seq[element] > seq[element+1]:
                count+=1

    except IndexError:
        element = 'null'
        if count == len(seq) - 1:
            return True
        else:
            return False




def main():
    print (is_decreasing([5,4,3,2,1]))
    print (is_decreasing([1,2,3]))
    print (is_decreasing([100,50,20]))
    print (is_decreasing([1,1,1,1]))
    print (is_decreasing([1,8,15,13,20]))


if __name__ == "__main__":
    main()


# Task: Increasing sequence?

def is_increasing(seq):

    count = 0
     try:
        for elem in range(0, len(seq)):

            if seq[elem] < seq[elem+1]:
                count+=1

    except IndexError:
        elem = 'null'
        if count == len(seq) - 1:
            return True
        else:
            return False



def main():
    print (is_increasing([1,2,3,4,5]))
    print (is_increasing([1]))
    print (is_increasing([5,6,-10]))
    print (is_increasing([1,1,1,1,1]))
    print (is_increasing([1,8,10,13,20]))


if __name__ == "__main__":
    main()


# Task: Consonants in a string

def count_consonants(str):

    consonants = "bcdfghjklmnpqrstvwxz"
    count = 0
    for string in range(0, len(str)):

        char = str[string]
        for cons in range(0, len(consonants)):

            ch = consonants[cons]
            if(char == ch or char == ch.upper()):
                count+=1


    return count


def main():
    print (count_vowels("Python"))
    print (count_vowels("Theistareykjarbunga"))
    print (count_vowels("grrrrgh!"))
    print (count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
    print (count_vowels("A nice day to code!"))
    print (count_vowels("HackBulgaria is a nice place to learn programing!"))

if __name__ == "__main__":
    main()



# Task: Vowels in a string

def count_vowels(str):

    count = 0
    for string in range(0, len(str)):

        char = str[string]
        if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'y'):
            count+=1
        char.upper()
        if(char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U' or char == 'Y'):
            count+=1
    return count
#  A, E, I, O, U, and sometimes Y



def main():
    print (count_vowels("Python"))
    print (count_vowels("Theistareykjarbunga"))
    print (count_vowels("grrrrgh!"))
    print (count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
    print (count_vowels("A nice day to code!"))
    print (count_vowels("HackBulgaria is a nice place to learn programing!"))

if __name__ == "__main__":
    main()



# Task: Turn a list of digits into a number

def to_number(digits):
    digitsn = []
    string = ""
    for number in range(0, len(digits)):

       string = string + str(digits[number])

    num = int(string)
    return num



def main():
    print (to_number([1,2,3]))
    print (to_number([9,9,9,9,9]))
    print (to_number([1,2,3,0,2,3]))
    print (to_number([6,7,9,0,2,3,11]))

if __name__ == "__main__":
    main()



# Task: Turn a number into a list of digits

def to_digits(n):
    list_digits = []
    num_len = int(len(str(n)))

    for numbers in range(0, num_len):

        result = n % 10
        n = n//10
        list_digits.append(result)
    list_digits.reverse()

    return list_digits


def main():
    print (to_digits(123))
    print (to_digits(9999))
    print (to_digits(123023))

if __name__ == "__main__":
    main()



# Task: Factorial Digits

def fact_digits(n):

    if n<0:
        n = abs(n)
    sum = 0
    n_len = int(len(str(n)))

    for number in range(0, n_len):

        result = n % 10
        n = int(n/10)
        fact = 1
        for nums in range(2, result+1):
            fact *= nums
        sum += fact
    return sum

def main():
    print (fact_digits(111))
    print (fact_digits(145))
    print (fact_digits(999))
    print (fact_digits(-2354))
    print (fact_digits(-5010))


if __name__ == "__main__":
    main()



# Task: Sum all digits of a number

def sum_of_digits(n):
    if n<0:
        n = abs(n)
    num_len = int(len(str(n)))
    sum_digits = 0
    for numbers in range(0, num_len):

        result = n % 10
        n = int(n/10)
        sum_digits += result
    return sum_digits

def main():
    print (sum_of_digits(1325132435356))
    print (sum_of_digits(123))
    print (sum_of_digits(6))
    print (sum_of_digits(-10))
    print (sum_of_digits(-148))
    print (sum_of_digits(-4636463))

if __name__ == "__main__":
    main()



# Task: Factorial

def factorial(n):
    fact = 1
    if n == 0 or n == 1:
        return fact
    for numbers in range(2, n+1):
        fact*=numbers
    return fact

def main():
    print (factorial(0))
    print (factorial(1))
    print (factorial(5))
    print (factorial(7))

if __name__ == "__main__":
        main()

