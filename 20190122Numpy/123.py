# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '22/1/2019 10:05 PM'
import numpy as np
np.__version__

l=[i for i in range(10)]
a=np.array(l)
a.reshape(2,5)

np.zeros(10,dtype='int')

np.zeros((3,4))

np.ones(shape=(2,3),dtype='int')

np.full((3,4),fill_value=666)

# arange

np.arange(0,1,0.2)  #[i for i in range(1,2,0.2)] 报错！！！

np.arange(10)

# linspace

np.linspace(0,20,11)

# np.random

np.random.randint(0,10)

np.random.randint(0,10,10)

np.random.randint(0,10,size=10)

np.random.randint(0,10,size=(3,4))

np.random.seed(666)
np.random.randint(0,10,size=(3,4))

np.random.seed(666)
np.random.randint(0,10,size=(3,4))

np.random.random(10)

np.random.random((2,4))

a=np.random.normal(0,1,(3,4))  # 均值，方差，size

a.ndim

a[0][0]

a[0,0]

X=np.arange(15).reshape(3,5)

X

X[1,1]

X[:2,3:]

X[::-1,::-1]

X[0]

X[:,0]

subX=X[:2,:3]
subX

subX1=X[:2,:3].copy()
subX1

# 合并

a=np.array([1,2,3])

b=np.array([3,2,1])
b

np.concatenate([a,b])

A=np.array([[1,2,3],[4,5,6]])
A

np.concatenate([A,A])

np.concatenate([A,A],axis=1)

z=np.array([66,66,66])
z

np.concatenate([A,z.reshape(1,-1)])

np.vstack([A,z])

B=np.full((2,2),100)
B

np.hstack([A,B])

# np.split(A,[3,7])   #np.split(A,[5])

data=np.arange(16).reshape(4,4)
data

X,y=np.hsplit(data,[-1])
X

y[:,0]

a=y.flatten()

b=np.tile(a,(2,1))  ##===  np.hstack([np.vstack([a]*2)]*1)

A=np.arange(4).reshape(2,2)

## 矩阵的逆

invA=np.linalg.inv(A)
invA

A.dot(invA)

b=np.arange(16).reshape(2,8)
pinvB=np.linalg.pinv(b)   #伪逆Pseudo
pinvB

b.dot(pinvB)