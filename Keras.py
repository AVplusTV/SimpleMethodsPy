import numpy as np
import pandas as pd

# загрузить набор данных, это может занять некоторое время

from keras.datasets import boston_housing
(train_x,train_y),(test_x,test_y)=boston_housing.load_data()

mean=train_x.mean(axis=0)
train_x-=mean
std=train_x.std(axis=0)
train_x/=std

test_x-=mean
test_x/=std

from keras import models, layers, backend as K
import seaborn


def build_model():
    model=models.Sequential()
    model.add(layers.Dense(128,activation='relu',input_shape=(train_x.shape[1],)))
    model.add(layers.Dense(128,activation='relu'))
    model.add(layers.Dense(2))
    model.compile(optimizer='rmsprop',loss='mse',metrics=['mae'])
    return model

model=build_model()
model.fit(train_x,train_y,epochs=120,batch_size=32,verbose=2)

test_mse, test_mae=model.evaluate(test_x, test_y)
print(test_mae, test_mse)

print(train_x)

inp = model.input 

outputs = [layer.output for layer in model.layers] 

print(outputs, inp)








