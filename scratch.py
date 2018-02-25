
x = ['a', 'b', 'c'] + [1, 2, 3]
print(x)

import numpy as np
r = np.array([[0,1,2,3,4,5], [6,7,8,9,10,11],[12,13,14,15,16,17],[18,19,20,21,22,23],[24,25,26,27,28,29],[30,31,32,33,34,35]])

#print(r[0:6,::-7])

print(r.reshape(36)[::7])

#print(r[::7])

#print(r[:,::7])

#print(r[[2,3],[2,3]])

#print(r[::2,::2])

#print(r[2::2,2::2])

print(r[2:4,2:4])


x**2
for x in range(10):
    print(x)