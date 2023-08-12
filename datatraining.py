import os
import numpy as np
import cv2
import tensorflow
from tensorflow import keras
from keras.utils import to_categorical

from keras.layers import Dense, Input
from keras.models import Model

is_init = False
size = -1

label = []
dictionary = {}
c = 0


for i in os.listdir():
    if i.split(".")[-1] == "npy" and not(i.split(".")[0] == "label"):    
        if not (is_init):
            is_init = True
            x = np.load(i)
            size = x.shape[0]
            y = np.array([i.split(".")[0]]*size).reshape(-1,1)
        else:
            x = np.concatenate((x, np.load(i)))
            y = np.concatenate((y, np.array([i.split(".")[0]]*size).reshape(-1,1)))
            
        label.append(i.split(".")[0])
        dictionary[i.split(".")[0]] = c
        c = c+1

for i in range(y.shape[0]):
    y[i, 0] = dictionary[y[i][0]]
y = np.array(y, dtype = "int32")

print(y.shape)
y = to_categorical(y)

x_new = x.copy()
y_new = y.copy()
counter=0

cnt = np.arange(x.shape[0])
np.random.shuffle(cnt)

for i in cnt:
    x_new[counter] = x[i]
    y_new[counter] = y[i]
    counter = counter+1
    
ip = Input(shape = (x.shape[1]))
m = Dense(512, activation = "relu")(ip)
m = Dense(256, activation = "relu")(m)

op = Dense(y.shape[1], activation = "softmax")(m)
model = Model(inputs = ip, outputs = op)

model.compile(optimizer = "rmsprop", loss = "categorical_crossentropy", metrics = ["accuracy"])
model.fit(x,y,epochs=50)

model.save("model.h5")
np.save("label.npy", np.array(label))
