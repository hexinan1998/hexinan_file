import tensorflow as tf
import numpy as np
class MNISTLoader():
    def __init__(self):
        mnist = tf.keras.datasets.mnist
        (self.train_data, self.train_label), (self.test_data, self.test_label) = mnist.load_data()
        # MNIST中的图像默认为uint8（0-255的数字）。以下代码将其归一化到0-1之间的浮点数，并在最后增加一维作为颜色通道
        self.train_data = np.expand_dims(self.train_data.astype(np.float32) / 255.0, axis=-1)      # [60000, 28, 28, 1]
        self.test_data = np.expand_dims(self.test_data.astype(np.float32) / 255.0, axis=-1)        # [10000, 28, 28, 1]
        self.train_label = self.train_label.astype(np.int32)    # [60000]
        self.test_label = self.test_label.astype(np.int32)      # [10000]
        self.num_train_data, self.num_test_data = self.train_data.shape[0], self.test_data.shape[0]

    def get_batch(self, batch_size):
        # 从数据集中随机取出batch_size个元素并返回
        index = np.random.randint(0, self.num_train_data, batch_size)
        return self.train_data[index, :], self.train_label[index]


class CNN(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.conv1 = tf.keras.layers.Conv2D(
            filters=32 ,  #卷积神经元的卷积核的数目
            kernel_size = [5,5] , #感受野的大小
            padding="same", # padding 策略的 （vaild 或 same）
            activation=tf.nn.relu  # 激活函数
        )
        self.pool1 = tf.keras.layers.MaxPool2D(pool_size=[2,2],strides=2)
        self.conv2 = tf.keras.layers.Conv2D(
            filters=64,
            kernel_size = [5,5],
            padding= 'same',
            activation=tf.nn.relu
        )
        self.pool2 = tf.keras.layers.MaxPool2D(pool_size=[2,2],strides=2)
        self.flatte = tf.keras.layers.Reshape(target_shape=(7 * 7 * 64,))
        self.dense1 = tf.keras.layers.Dense(units=1024,activation=tf.nn.relu)
        self.dense2 = tf.keras.layers.Dense(units=10)
    def call(self,input):
        x = self.conv1(input)   # [batch_size, 28, 28, 32]
        x = self.pool1(x)       # [batch_size, 14, 14, 32]

        x = self.conv2(x)       # [batch_size, 14, 14, 64]
        x = self.pool2(x)       # [batch_size, 7, 7, 64]

        x = self.flatte(x)      # [batch_size, 7 * 7 * 64]
        x = self.dense1(x)      # [batch_size, 1024]
        x = self.dense2(x)      # [batch_size, 10]
        output = tf.nn.softmax(x)
        return output