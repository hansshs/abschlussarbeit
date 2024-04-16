#%%
import visualkeras as vk
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.losses import categorical_crossentropy
from keras.optimizers import Adadelta
from keras.utils import to_categorical
from PIL import ImageFont

from tensorflow.python.keras.layers import ZeroPadding2D
from collections import defaultdict

#%%
num_classes = 10
img_rows, img_cols = 28, 28

# Define the model architecture
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))
model.add(vk.SpacingDummyLayer(spacing=100))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

#%%
color_map = defaultdict(dict)
color_map[Conv2D]['fill'] = '#F6C85F'  # Yellow
color_map[ZeroPadding2D]['fill'] = '#D0D3D4'  # Light gray
color_map[Dropout]['fill'] = '#CA472F'  # Red 
color_map[MaxPooling2D]['fill'] =  '#9DD866' #Green
color_map[Dense]['fill'] = '#8DDDD0'  # Light blue
color_map[Flatten]['fill'] = '#FFA056'  # Orange

font = ImageFont.truetype("arial.ttf", 18)


vk.layered_view(model, 
                legend=True, font=font, color_map=color_map, scale_xy=10,
                spacing=15, draw_funnel = False, shade_step=35).show()

# %%
