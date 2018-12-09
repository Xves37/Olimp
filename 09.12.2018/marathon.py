fin = open('marathon.in', 'r') 
fout = open('marathon.out', 'w')
l = [line.strip() for line in fin.readlines()]

n = int(l[0])

l = l[1:]
a = []
time_a = []
for i in range(n):
    time_a.append(l[i])

for i in range(n):
    hours, minutes, seconds = map(int, l[i].split())
    value = hours * 3600 + minutes * 60 + seconds
    a.append(value)

for i in range(len(a) - 1):
    min = a[i]
    pos = i
    time_min = time_a[i]

    for j in range(i+1, len(a)):
        if min > a[j]:
            min = a[j]
            time_min = time_a[j]
            pos = j
    a[pos] = a[i]
    a[i] = min

    time_a[pos] = time_a[i]
    time_a[i] = time_min

for i in range(n):
    print(time_a[i], file = fout)

fout.close()