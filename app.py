import streamlit as st
import tensorflow
from PIL import Image
from tensorflow.keras.models import load_model
import numpy as np
import time
import cv2


@st.cache(allow_output_mutation=True)
def get_model():
        model = load_model('MN21.h5')
        return model 
    
def predict(image):
        loaded_model = get_model()
        image = cv2.imread(image)
        image = cv2.resize(image/255, (224, 224))
        image = np.reshape(image,[1,224,224,3])

        classes = loaded_model.predict_classes(image)
        return classes 

st.title("NSFW Classifier")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:

        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        st.write("")

        if st.button('predict'):
                st.write("Result...")
                start = time.time()
                label = predict(uploaded_file)
                end = time.time()
                # label = label.item()
                print(label)
                # st.write(end - start)

                # res = sign_names.get(label)
                st.markdown(label)
