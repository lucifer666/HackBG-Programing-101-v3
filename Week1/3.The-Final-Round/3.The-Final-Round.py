# Task: Magic Square

def magic_square(matrix):
    list_matrix = []
    sum_cols = 0
    for rows in matrix:
        for cols in range(0, len(rows)):
            sum_cols += rows[cols]

        list_matrix.append(sum_cols)
        sum_cols = 0

    count_true = 0
    for sums in range(1, len(list_matrix)):
        if list_matrix[0] == list_matrix[sums]:
                count_true += 1
    if count_true == len(list_matrix) - 1:
        return True
    else:
        return False


print (magic_square([[1,2,3], [4,5,6], [7,8,9]]))
print (magic_square([[4,9,2], [3,5,7], [8,1,6]]))
print ( magic_square([[7,12,1,14], [2,13,8,11], [16,3,10,5], [9,6,15,4]]))
print (magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
print (magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))
print (magic_square([[16, 23, 17], [3, 32, 21], [17, 24, 15]]))

# Task: Spam and Eggs

def prepare_meal(number):

    spam = ''
    eggs = ''
    variable = number
    count_spam = 0
    count_eggs = 0

    while variable != 1:

        if variable < 3:
            return '""'
        if variable == 5:
            return "eggs"

        variable = variable // 3
        count_spam += 1
        if variable % 5 == 0:
            count_eggs+=1
            variable = variable // 5

    if variable == 1:
        while count_spam != 0:

            spam +="spam "
            count_spam -= 1

        while count_eggs != 0:
            if count_eggs == 1:
                eggs = 'and' + eggs
            eggs += " eggs"
            count_eggs -= 1

        return spam+eggs


print(prepare_meal(3))
print(prepare_meal(27))
print(prepare_meal(7))
print(prepare_meal(5))
print(prepare_meal(15))
print(prepare_meal(45))
print(prepare_meal(2025))
print(prepare_meal(2025*27*25))

# Task: The group function
# задачата работи магически

def group(elements):

    group_el = []
    group_el1 = []

    group_el.append(elements[0])

    try:

            for elem in range(0, len(elements)):

               # print (group_el1)

                if elements[elem] == elements[elem+1]:
                    group_el.append(elements[elem+1])

                if elem == len(elements)-2:
                    group_el1.append(group_el)
                    break

                if elements[elem] != elements[elem+1]:
                    if len(group_el) != 0:
                        group_el1.append(group_el)
                        group_el = []

                    if elem == len(elements)-2:
                        group_el1.append([elements[elem+1]])
                        break
                    if elements[elem+1] == elements[elem+2]:
                        group_el.append(elements[elem+1])
                        continue
                    else:
                        group_el1.append([elements[elem+1]])

            return group_el1
       # return (group_el1)
            #print (group_el1)
    except IndexError:
        elem = 'null'


print (group([1,1,1,2,3,1,1]))
print (group([1, 2, 1, 2, 3, 3]))
print (group([1,2,3,4,4,4,4,6,8,10,10,1,1,1,3,3,10,12,15,15,15,2,9,9,3,9,9,9,9,4,5,6,7,10,10]))



# Task: Reduce file path
def reduce_file_path(path):

        slash = "/"
        dot_dot = ".."
        dot = "."
        dot_dot_slash = dot_dot + slash
        dot_slash = dot + slash
        dots = 0
        count_slash = 0
        counts = 0

        if path == slash:
            return slash

        if dot_dot_slash in path:
            return slash

        if dot_slash in path:
            dots = path.count(dot_slash)
            path = path[:-dots*2]
            path = path[:-1]

        if slash in path:
                if "//" in path:
                    while "//" in path:
                        path = path.replace("//", "/")

                    if slash == path[len(path)-1] and path != slash:
                        path = path[:-1]
                        return path

                    elif slash != path[len(path)-1:]:
                        return path
                    else:
                        return path

                elif slash == path[len(path)-1:]:

                    path = path[:-1]
                    return path
                else:
                    return path



print (reduce_file_path("/"))
print (reduce_file_path("/srv/../"))
print (reduce_file_path("/srv/www/htdocs/wtf/"))
print (reduce_file_path("/srv/www/htdocs/wtf"))
print (reduce_file_path("/srv/./././././"))
print (reduce_file_path("/etc//wtf/"))
print (reduce_file_path("/etc/../etc/../etc/../"))
print (reduce_file_path("//////////////"))
print (reduce_file_path("/../"))
print (reduce_file_path("/etc///././././"))

# Task: Credit card validation

def is_credit_card_valid(number):

    number_len = int(len(str(number)))
    count_numbers = 0
    number_list = []
    str_number = ""
    for nums in range(0, number_len):

        count_numbers += 1
        result = number % 10
        number = number // 10
        number_list.append(result)

    if count_numbers % 2 == 0:
        return ("This is not a valid credit card! The number of the digits is not odd!")


    for elem in range(0, len(number_list)):
        if elem % 2 != 0:
         number_list[elem] = number_list[elem]*2
    number_list.reverse()
    sum_numbers = 0
    for it in range(0, len(number_list)):

        str_number += (str(number_list[it]))
    int_number = int(str_number)
    for digits in range(0, len(str_number)):

        result_digit = int_number % 10
        int_number = int_number // 10
        sum_numbers += result_digit
    print (sum_numbers)


    if sum_numbers % 10 == 0:
        return True
    else:
        return False


print (is_credit_card_valid(79927398713))
print (is_credit_card_valid(79927398715))
print (is_credit_card_valid(451343747581))
print (is_credit_card_valid(44134374758))
print (is_credit_card_valid(45034374758))

# Task: Word from a^nb^n

def is_an_bn(word):

    string_a = ""
    string_b = ""
    count_a = 0
    count_b = 0

    for ab in word:

        count_a = word.count("a")
        count_b = word.count("b")
    while count_a != 0 and count_b != 0 and count_a == count_b:
        string_a = string_a + 'a'
        string_b = string_b + 'b'
        count_a-=1
        count_b-=1

    string_ab = string_a + string_b
    if word == '""':
        return True
    elif word == string_ab:
        return True
    else:
        return False

print (is_an_bn(""))
print (is_an_bn("rado"))
print (is_an_bn("aaabb"))
print (is_an_bn("aaabbb"))
print (is_an_bn("aabbaabb"))
print (is_an_bn("bbbaaa"))
print (is_an_bn("aaaaabbbbb"))

# Task: Iterations of NaN Expand

def iterations_of_nan_expand(expanded):

    empty_string = '""'
    not_a = "Not a"
    count_not_a = 0
    if expanded == empty_string:
        return 0
    if not_a not in expanded:
        return False
    ex_strip = expanded.strip()

    for expand in range(0, len(expanded)):

        if '  ' in expanded:
          return False

        count_not_a = expanded.count(not_a)

    return (count_not_a)

print (iterations_of_nan_expand('""'))
print (iterations_of_nan_expand("Not a Nan"))
print (iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
print (iterations_of_nan_expand("Show these people!"))
print (iterations_of_nan_expand("Not a Not a Not a Not a              Nan"))

# Task: NaN Expand
def nan_expand(times):

    not_a_nan = "Not a Nan"
    not_a = "Not a "
    empty = '""'
    repeat = ""
    if times == 0:
        return empty
    elif times == 1:
        return not_a_nan
    elif times>1:
        for elem in range(1, times):
            repeat =  repeat + not_a

        string = repeat + not_a_nan
        return string


print (nan_expand(0))
print (nan_expand(1))
print (nan_expand(2))
print (nan_expand(3))
print (nan_expand(10))

# Task: Unique words

def unique_words_count(arr):

    set_arr = set(arr)
    count_words = 0
    for words in range(0, len(set_arr)):

        count_words+=1

    return count_words


print (unique_words_count(["apple", "banana", "apple", "pie"]))
print (unique_words_count(["python", "python", "python", "ruby"]))
print (unique_words_count(["HELLO!"] * 10))
print (unique_words_count(["kostaa","Kostaa","kostaa","hackbg","hackbg"]))

# Task: Count words

def count_words(arr):

    dict_words = {}

    for elements in range (0, len(arr)):

        count_words = arr.count(arr[elements])
        dict_words[arr[elements]] = count_words

    return dict_words

print (count_words(["apple", "banana", "apple", "pie"]))
print (count_words(["python", "python", "python", "ruby"]))
print (count_words(["Filip", "hack", "Hack", "hack","filip", "filip"]))























































