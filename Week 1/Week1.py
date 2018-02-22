'''
Data Science - Week 1

Date: 18FEB2018

'''
import numpy as np

mylist = [1,2,3]
x =np.array(mylist)
print('np.array: \n',x,'\n')

y = np.array([4,5,6])
print ('np.array: \n',y,'\n')

m = np.array([[7, 8, 9],[10, 11, 12]])
print('np.array: \n',m,'\n')

print('m.shape: \n',m.shape,'\n')

n = np.arange(0, 30, 2)
print('np.arange: \n',n,'\n')

n = n.reshape(3, 5)
print('n.reshape: \n',n,'\n')

o = np.linspace(0, 4, 9)
print('o:', o)
print('o.linspace:', o, '\n')

o = o.resize(3, 3)
print('o.resize: \n', o, '\n')

print('np.ones: \n', np.ones((2, 3)), '\n')

print('np.zeros: \n', np.zeros([2, 3]), '\n')

print('np.eye: \n', np.eye(3), '\n')

print('np.diag: \n', np.diag(y), '\n')

print('np.array * 3: \n', np.array([1, 2, 3]*3), '\n')

print('np.repeat, 3: \n', np.repeat([1, 2, 3],3), '\n')

print('np.ones,int: \n', np.ones([2, 3],int), '\n')

p = np.ones([2, 3],int)
print('np.vstack: \n', np.vstack([p, 2*p]), '\n')

print('np.hstack: \n', np.hstack([p, 2*p]), '\n')

print('x+y: ', x+y, '\n')
print('x*y: ', x*y, '\n')
print('x**2: ', x**2, '\n')
print('x.dot(y): ', x.dot(y), '\n')
print('x**2: ', x**2, '\n')
print('np.array([y, y**2]): \n', np.array([y, y**2]), '\n')

z = np.array([y, y**2])
print('z.T.shape :', z.T.shape, '\n')

print('z.dtype: \n', z.dtype, '\n')
print('z.astype: \n', z.astype('f'), '\n')
z = z.astype('f')
print('z.dtype: \n', z.dtype, '\n')

a = np.array([-4, -2, 1, 3, 5])
print('a.sum: ', a.sum(), '\n')
print('a.max: ', a.max(), '\n')
print('a.min: ', a.min(), '\n')
print('a.mean: ', a.mean(), '\n')
print('a.std: ', a.std(), '\n')
print('a.argmax: ', a.argmax(), '\n')
print('a.argmin: ', a.argmin(), '\n')

# Indexing / Slicing

s = np.arange(13)**2
print('np.arange(13)**2 :', s, '\n')

print(s[0], s[4], s[0:3])
print(s[1:5])
print(s[-4:])
print(s[-5::-2])

r = np.arange(36)
r.resize((6, 6))
print(r)

print('\n', r[2,2])
print('\n', r[3, 3:6])
print('\n', r[:2, :-1])
print('\n', r[-1, ::2])
print('\n', r[r>30])
r[r>30]=30
print('\n', r)

r2 = r[:3,:3]
print(r2)

print(r)

r_copy = r.copy()
print('r_copy: \n', r_copy, '\n')

old = np.array([[1, 1, 1],
                [1, 1, 1]])

new = old.copy()
new[:, 0] = 0

print('old:', old, '\n')

# Iterating Over Arrays

test = np.random.randint(0, 10, (4, 3))
print('np.random.randint(0 , 10, (4, 3)) \n', test, '\n')

print('for row in test:')
for row in test:
    print(row)

print('\nfor i in range(len(test)):')
for i in range(len(test)):
    print(test[i])

print('\n')
for i, row in enumerate(test):
    print('row', i, 'is', row)

print('\n')
test2 = test**2
print('test2: \n', test2)

print('\n')
for i,j in zip(test, test2):
    print(i, '+', j, '=', i+j)





