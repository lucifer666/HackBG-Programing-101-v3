# Task: Alternative to du -h command
import os
import sys

def return_size_of_a_file():

    if len(sys.argv) > 1:
        path = sys.argv[1]
        path_total_size = 0
        if os.path.isdir(path):
            for dirlist, subdirlist, filenames in os.walk(path):
                for filename in filenames:
                    fn = os.path.join(dirlist, filename)
                    path_total_size += os.path.getsize(fn)

            return get_size(path_total_size)
        elif os.path.isfile(path):
            path_total_size = os.path.getsize(path)
            return get_size(path_total_size)
    else:
        print ("Give me a directory or a file!")

def get_size(path_get_size):
    if path_get_size >= 8 and path_get_size < 2**10:
        return (("The size is: %d bytes") % path_get_size)
    elif path_get_size >= 2**10 and path_get_size < 2**20:
        path_get_size = float(path_get_size/10**3)
        return (("The size is: %.2f kb") % path_get_size)
    elif path_get_size >= 2**20 and path_get_size < 2**30:
        path_get_size = float(path_get_size/10**6)
        return ("The size is: %.2f mb" % path_get_size)
    elif path_get_size >= 2**30 and path_get_size < 2**40:
        path_get_size = float(path_get_size/10**9)
        return ("The size is: %.2f gb" % path_get_size)

def main():
    print (return_size_of_a_file())

if __name__ == "__main__":
    main()

# Task: Sum integers from file

def read_sum(filename):
    sum_numbers = 0
    list_num = []
    file_name = open(filename)
    for line in file_name:
        list_num.append(line)

    numbers = list_num[0].split(' ')
    for num in range(0, len(numbers)-1):
        sum_numbers += int(numbers[num])
    print(numbers)
    file_name.close()
    return sum_numbers

def main():
   print (read_sum("numbers.txt"))

if __name__ == "__main__":
    main()


# Task: Generate file with random integers
import sys
from random import randint

def generate_numbers(filename,n):

            file_n = open(filename, "w")
            file_n.truncate() # изтриваме съдържанието(ако има такова)преди да пишем в файла
            for numbers in range(0,n):

                number = randint(0,1000)
                file_n.write("%d" % number +" ")
            file_n.close()

def main():
    generate_numbers("numbers.txt",10)

if __name__ == '__main__':
    main()


# Task: Cat multiple files
import sys

def read_files(n):
    if len(sys.argv) > 1:
        while n != 0:
            filename = sys.argv[n]
            file_name = open(filename, "r")
            text = file_name.read()
            print (text)
            file_name.close()
            n-=1
    else:
        print ("Give me a file to read!")

def main():
    n = int(input("Here you must type the number of the files, that you entered above?!: "))
    read_files(n)

if __name__ == "__main__":
    main()


# Task: Implement the cat command - Print file contents
# Task1.1:
import sys

def read_file():
    if len(sys.argv) > 1:
        for file_name in range(1,3): # can read 2 files
            filename = sys.argv[file_name]
            file_n = open(filename, "r")
            text = file_n.read()
            print (text)
            file_n.close()

    else:
        print ("Give me a file to read!")

def main():
     print (read_file())

if __name__ == "__main__":
    main()


# Task1.2:
def read_file(filename):


        file_n = open(filename, "r")
        text = file_n.read()
        print (text)
        file_n.close()


def main():
    read_file("file.txt")

if __name__ == '__main__':
    main()
