
import random

t1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
t2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
t3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

password = []
l1 = len(t1)
l2 = len(t2)
l3 = len(t3)

count = 0
len = int(input('Введите длину пароля '))
need = int(input('Сколько паролей нужно? '))

while count != len * need:
    count = count + 1
    tier = random.randint(1, 3)
    if tier == 1:
        password.append(t1[random.randint(0, l1 - 1)])
    elif tier == 2:
        password.append(t2[random.randint(0, l2 - 1)])
    elif tier == 3:
        password.append(t3[random.randint(0, l3 - 1)])

s = ''.join(str(x) for x in password)
count2 = 0

while count2 < len * need:
    print(s[count2:count2 + len])
    count2 = count2 + len
