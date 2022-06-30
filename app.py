import cv2
import time
from PIL import Image, ImageOps
import numpy as np
import streamlit as st
import tensorflow as tf

@st.cache(allow_output_mutation=True)
def load_model():
    model=tf.keras.models.load_model('MN21.h5')
    return model
with st.spinner('Model is being loaded..'):
    model=load_model()

st.write("""# SaferNet with AI""")

file = st.file_uploader("Please upload an image to classify", type=["jpg", "png", "jpeg"])
def import_and_predict(image_data, model):
    size = (224,224)    
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    image = np.asarray(image)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #img_resize = (cv2.resize(img, dsize=(75, 75),    interpolation=cv2.INTER_CUBIC))/255.
    
    img_reshape = img[np.newaxis,...]
    
    st.write(img_reshape.shape)
    
    start = time.time()
    prediction = model.predict(img_reshape)
    end = time.time()
    time_take = end - start
    return prediction, time_take 

if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions, time_take = import_and_predict(image, model)
    st.write("Time taken to predict is ", time_take, "second")
    st.write(predictions)
    print(predictions)
    
    print(np.argmax(predictions))
    st.write(np.argmax(predictions))
    
    st.write('each member of pred')
    st.write(predictions.shape)
    st.write(predictions[0])
    st.write(predictions[1])
    
    if predictions[0][0] < 0.5:
        st.write("This is SFW image :sunglasses:")
    else:
        st.write("This is NSFW image")
