import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

dataset = tf.keras.datasets.mnist

(_,_),(test_data,test_label) = dataset.load_data()


fig , axes = plt.subplots(nrows=2, ncols=2)
for index,img_i in  enumerate(np.random.randint(0,test_data.shape[0],4)):
    i = 1 if index>=2 else 0
    j = index%2
    axes[i][j].imshow(test_data[img_i])
    axes[i][j].set(title=test_label[img_i])
plt.show()