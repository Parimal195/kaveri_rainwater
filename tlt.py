import math
import numpy as np
import matplotlib.pyplot as plt
import datetime
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM,Dense ,Dropout
from sklearn.preprocessing import MinMaxScaler

data=[]
for i in range(1901,2014):
	with open("Cauvery/rfp_"+str(i)+".TXT") as f:
		a = [x.replace(" ", "").split("\t") for x in f.readlines()]
	b = []
	for line in a:
		line.remove("\n")
		array = [float(x) for x in line]
		b.append(array)
	b = np.array(b)
	data.append(b)


data =np.array(data)
m = np.array([np.mean(x, axis = 1) for x in data])
a = []
for x in m:
  for y in x:
    a.append(y)
a = np.array(a)

sc = MinMaxScaler(feature_range=(0,1))
a_scaled = sc.fit_transform(a)

x_train = []
y_train = []
n_future = 4	# next 206 days temperature forecast
n_past = 30 # Past 20631 days 
for i in range(0,len(a_scaled)-n_past-n_future+1):
    x_train.append(a_scaled[i : i + n_past])     
    y_train.append(a_scaled[i + n_past : i + n_past + n_future ])
x_train , y_train = np.array(x_train), np.array(y_train)
# x_train = np.reshape(x_train, (x_train.shape[0] , x_train.shape[1],1) )
x_train = np.reshape(-1,1)
print(x_train.shape)
print(y_train.shape)


regressor = Sequential()
regressor.add(Bidirectional(LSTM(units=30, return_sequences=True, input_shape = (x_train.shape[1],1) ) ))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units= 30 , return_sequences=True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units= 30 , return_sequences=True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units= 30 , return_sequences=True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units= 30))
regressor.add(Dropout(0.2))
regressor.add(Dense(units = n_future,activation='linear'))

regressor.compile(optimizer='adam', loss='mean_squared_error',metrics=['acc'])
# regressor.fit(x_train, y_train, epochs=500,batch_size=32, verbose = True )

print(regressor.summary())


# np.save("array.npp")
# print(len(a))



# print(m.shape)
# x = np.array([x for x in range (366)])
# # y = np.array([y for y in range(m[0])])
# for i in range(113):
# 	for j in range(365):
# 		plt.plot(x,m[i][j])
# 		plt.show()
#  #print(len(m[0]))