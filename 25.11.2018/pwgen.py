import random

fin = open('pwgen.in', 'r') 
fout = open('pwgen.out', 'w') 

l = [line.strip() for line in fin.readlines()] 

n = int(l[0]) 
a, b, c = int(l[1].split()[0]), int(l[1].split()[1]), int(l[1].split()[2]) 

alfLow = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

password = ''

for j in range(a):
    while (1):
        let = random.choice(alfLow).upper()
        if (0 == len(password)):
            password += let
            break
        if (let != password[len(password) - 1]):
            password += let
            break

for j in range(b):
    while (1):
        let = random.choice(alfLow)
        if (0 == len(password)):
            password += let
            break
        if (let != password[len(password) - 1]):
            password += let
            break

for j in range(n - a - b):
    while (1):
        let = str(random.randrange(0,9))
        if (0 == len(password)):
            password += let
            break
        if (let != password[len(password) - 1]):
            password += let
            break

print(password, file = fout)

fout.close()