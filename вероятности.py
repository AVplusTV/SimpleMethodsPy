import random
from statistics import mean
import matplotlib.pyplot as plt


qs = []
for j in range(1000):
    q = 0
    for i in range(100000):
        n= random.randint(1, 5)
        m= random.randint(1, 5)
        if n == 5 or m == 5:
            q +=1

    q1 = q/100000
    qs.append(q1)

print(round(mean(qs), 3))


plt.hist(qs, range = (0.355, 0.365), bins=50)
plt.ylabel('Частотность')
plt.xlabel('вероятность выпадений 5 при 100000 экспериментах')
plt.grid();