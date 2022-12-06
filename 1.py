import time
import os, psutil


def add_number(book, number):
    book.add(number)


def find_number(book, number):
    if number in book:
        return "Y"
    else:
        return "N"


def del_number(book, number):
    if number in book:
        book.remove(number)


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("1_input.txt")
m = open("1_output.txt", "w")
count = int(f.readline())
book = set()
for i in range(count):
    string = f.readline()
    elements = list(map(str, string.split()))
    if elements[0] == "A":
        add_number(book, int(elements[1]))
    if elements[0] == "?":
        m.write(str(find_number(book, int(elements[1]))) + "\n")
    if elements[0] == "D":
        del_number(book, int(elements[1]))


f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")
