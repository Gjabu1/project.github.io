import random
import numpy as np
def password(length, count, t4_activ = True):
    t1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
    t2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
    t3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    t4 = ['%', '*', ')', '(', '?', '@', '#', '$', '~']
    answer = []

    while len(answer) != length * count:
        if t4_activ == True:
            x = random.randint(1, 4)
            if x == 1:
                answer.append(t1[random.randint(0, len(t1) - 1)])
            elif x == 2:
                answer.append(t2[random.randint(0, len(t2) - 1)])
            elif x == 3:
                answer.append(t3[random.randint(0, len(t3) - 1)])
            elif x == 4:
                answer.append(t4[random.randint(0, len(t4) - 1)])

        elif t4_activ == False:
            x = random.randint(1, 3)
            if x == 1:
                answer.append(t1[random.randint(0, len(t1) - 1)])
            elif x == 2:
                answer.append(t2[random.randint(0, len(t2) - 1)])
            elif x == 3:
                answer.append(t3[random.randint(0, len(t3) - 1)])

    for i in np.array_split(answer, count):
        print(''.join(i))

password(10, 15)