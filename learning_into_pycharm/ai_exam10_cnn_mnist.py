from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
from keras.utils import to_categorical

(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

y_train = to_categorical(Y_train)
y_test = to_categorical(Y_test)

x_train = X_train.reshape(60000, 28, 28, 1)
x_test = X_test.reshape(10000, 28, 28, 1)

x_train = x_train / 255
x_test = x_test / 255

model = Sequential()
model.add(Conv2D(5, input_shape=(28, 28, 1), activation='relu',
                 kernel_size=(3, 4), padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2), padding='same'))
model.add(Conv2D(6, kernel_size=(3, 3), activation='relu',
                 padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2), padding='same'))
model.add(Flatten())
model.add(Dense(16, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.summary()

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

fit_hist = model.fit(x_train, y_train, epochs=15, batch_size=512,
                     validation_split=0.2)
accuracy = model.evaluate(x_test, y_test)[1]
model.save('cnn_mnist_micro_{:.3f}.h5'.format(accuracy))
