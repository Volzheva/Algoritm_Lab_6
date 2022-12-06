import time
import os, psutil


def add_number(book, number, name):
    book[number] = name


def find_number(book, number):
    if number in book:
        return book[number]
    else:
        return "not found"


def del_number(book, number):
    if number in book:
        book.pop(number)


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("2_input.txt")
m = open("2_output.txt", "w")
count = int(f.readline())
book = {}
for i in range(count):
    string = f.readline()
    elements = list(map(str, string.split()))
    if elements[0] == "add":
        add_number(book, int(elements[1]), elements[2])
    if elements[0] == "find":
        m.write(str(find_number(book, int(elements[1]))) + "\n")
    if elements[0] == "del":
        del_number(book, int(elements[1]))


f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")
