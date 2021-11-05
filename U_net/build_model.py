import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import os 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# Define Sequential model with 3 layers
A = 3
model = keras.Sequential(
    [
        
        #contraction path
        # c1
        layers.Conv3D(A,kernel_size=3,strides=1), # stride 步长
        layers.Dropout(0.1),
        layers.Conv3D(A,kernel_size=3,strides=1),
        layers.MaxPooling3D(pool_size=2,strides=1),

        layers.Conv3D(A*2,kernel_size=3,strides=1),
        layers.Dropout(0.1),
        layers.Conv3D(A*2,kernel_size=3,strides=1),
        layers.MaxPool3D(pool_size=2,strides=1),

        layers.Conv3D(A,kernel_size=3,strides=1),
        layers.Dropout(0.1),
        layers.Conv3D(A,kernel_size=3,strides=1),
        layers.MaxPool3D(pool_size=2,strides=1),
        #c4
        layers.Conv3D(A,kernel_size=3,strides=1),
        layers.Dropout(0.1),
        layers.Conv3D(A,kernel_size=3,strides=1),
        layers.MaxPool3D(pool_size=2,strides=1),

        layers.Conv3D(A,kernel_size=3,strides=1),
        layers.Dropout(0.1),
        layers.Conv3D(A,kernel_size=3,strides=1),

        #Expansive Path
        layers.Conv3DTranspose(A,kernel_size=3,strides=1),
        # layers.Concatenate(,),
    ]
)
# Call model on a test input
x = tf.ones((32,128,128,128,2))
y = model(x) 
model.summary()