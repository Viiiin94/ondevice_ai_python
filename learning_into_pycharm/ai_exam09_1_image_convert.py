from PIL import Image
import glob
import numpy as np
from sklearn.model_selection import train_test_split

img_dir = '/media/user23/data/cat_dog/train/'
categories = ['cat', 'dog']

image_width = 64
image_height = 64

pixel = image_width * image_height * 3

X = []
Y = []
files = None

for idx, category in enumerate(categories):
    files = glob.glob(img_dir + category + '*.jpg')
    for i, f in enumerate(files):
        try:
            img = Image.open(f)
            img = img.convert('RGB')
            data = img.resize((image_width, image_height))
            X.append(data)
            Y.append(idx)
            if i % 300 == 0:
                print(category, ':', f)

        except (IOError, OSError) as e:
            print(category, i, e)

X = np.array(X)
Y = np.array(Y)
X = X / 255 # 스케일링
print(X[0])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

np.save('./ binary_X_train.npy', X_train)
np.save('./ binary_X_test.npy', X_test)
np.save('./ binary_Y_train.npy', Y_train)
np.save('./ binary_Y_test.npy', Y_test)








