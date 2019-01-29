import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

X=np.random.randint(0,100,(50,2))
X=np.array(X,dtype='float')
X

X[:,0]=(X[:,0]-np.min(X[:,0]))/(np.max(X[:,0])-np.min(X[:,0]))

X[:,1]=(X[:,1]-np.min(X[:,1]))/(np.max(X[:,1])-np.min(X[:,1]))

X