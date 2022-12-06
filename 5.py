import time
import os, psutil


def processing(info, name, voices):
    if name in info:
        info[name] += voices
    else:
        info[name] = voices


t_start = time.perf_counter()
process = psutil.Process(os.getpid())
f = open("5_input.txt")
m = open("5_output.txt", "w")

info = {}
while True:
    string = f.readline()
    if not string:
        break
    elements = list(map(str, string.split()))
    name = elements[0]
    voices = int(elements[1])
    processing(info, name, voices)

info = dict(sorted(info.items()))
for name, voices in info.items():
    m.write(name + ' ' + str(voices) + "\n")

f.close()
m.close()

print("Time of working: %s second" % (time.perf_counter() - t_start))
print("Memory", process.memory_info().rss/(1024*1024), "mb")
