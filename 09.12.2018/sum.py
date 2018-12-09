n, sum = map(int, input().split())
a = []

min = 0
pos = 0
my_sum = 0
count = 0

for i in range(n):
    a.append(int(input()))

for i in range(len(a) - 1):
    min = a[i]
    pos = i

    for j in range(i+1, len(a)):
        if min > a[j]:
            min = a[j]
            pos = j
    a[pos] = a[i]
    a[i] = min

a = a[::-1]

for i in a:    
    if my_sum < sum:
        count += 1
        my_sum += i

if my_sum < sum:
    print('UPS')
else:
    print(count)