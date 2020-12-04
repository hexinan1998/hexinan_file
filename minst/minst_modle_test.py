import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from class_use import *

#加载模型
model = CNN()
checkpoint = tf.train.Checkpoint(myAwesomeModel=model)
checkpoint.restore(tf.train.latest_checkpoint("./save"))


# 准本数据
dataset = tf.keras.datasets.mnist
(_,_),(test_data,test_label) = dataset.load_data()
# test_data = np.expand_dims(test_data.asype(np.float32) / 255.0, axis=-1)
# test_data = np.expand_dims(test_data.astype(np.float32) / 255.0, axis=1)
test_data = np.expand_dims(test_data.astype(np.float32) / 255.0, axis=-1)
# test_label = test_label.astype(np.int32)

# print(test_data[0].shape)
# 开始使用   下面指定 图片序号
img_in = 1231 # 此值 修改  0 - 9999

# batch_size单值训练 z 不可更改
z = 1

prediction = model(test_data[img_in*z:(img_in+1)*z])
pre = np.argmax(prediction,1)[0]
print("预测值: ",pre," 真实值: " ,test_label[img_in])
plt.imshow(test_data[img_in].reshape((28,28)))
plt.title(pre)
plt.show()