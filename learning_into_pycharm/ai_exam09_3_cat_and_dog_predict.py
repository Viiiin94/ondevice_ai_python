from PIL import Image
from tensorflow.keras.models import load_model
import numpy as np
import glob

categories = ['cat', 'dog']

model = load_model('./cat_and_dog_binary_classification_0.853600025177002.h5')
model.summary()

img_dir = '/media/user23/data/cat_dog/train/'
image_width = 64
image_height = 64

dog_files = glob.glob(img_dir + 'dog*.jpg')
dog_sample = np.random.randint(len(dog_files))
dog_sample_path = dog_files[dog_sample]

cat_files = glob.glob(img_dir + 'cat*.jpg')
cat_sample = np.random.randint(len(cat_files))
cat_sample_path = cat_files[cat_sample]

print(dog_sample_path)
print(cat_sample_path)

try:
    img1 = Image.open(dog_sample_path)
    # img1 = Image.open('/home/user23/Downloads/istockphoto-1503385646-612x612.jpg')
    img1.show()
    img1 = img1.convert('RGB')
    img1 = img1.resize((image_width, image_height))
    data1 = np.asarray(img1)
    data1 = data1 / 255
    dog_data = data1.reshape(1, 64, 64, 3)

    img2 = Image.open(cat_sample_path)
    # img2 = Image.open('/home/user23/Downloads/Molly_006-2829x1886-2726x1886-1920x1328.jpg')
    img2.show()
    img2 = img2.convert('RGB')
    img2 = img2.resize((image_width, image_height))
    data2 = np.asarray(img2)
    data2 = data2 / 255
    cat_data = data2.reshape(1, 64, 64, 3)

    print('dog data : ', model.predict(dog_data).round())
    print('cat data : ', model.predict(cat_data).round())

except (IOError, OSError) as e:
    print(e)

print('dog data cate : ', categories[int(model.predict(dog_data).round()[0][0])])
print('cat data cate : ', categories[int(model.predict(cat_data).round()[0][0])])












