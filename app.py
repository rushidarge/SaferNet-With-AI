import streamlit as st
import tensorflow
from tensorflow.keras.models import load_model
from skimage.transform import resize
import numpy as np
import time
import cv2
from PIL import Image, ImageOps


@st.cache(allow_output_mutation=True)
def get_model():
        model = load_model('MN21.h5')
        return model 
    
# def predict(image):
#         loaded_model = get_model()
#         size = (224,224)    
#         image = ImageOps.fit(image, size, Image.ANTIALIAS)
#         image = np.asarray(image)/255
#         # image = cv2.imread(image)
#         # image = cv2.resize(image/255, (224, 224))
#         image = np.reshape(image,[1,224,224,3])

#         classes = loaded_model.predict_classes(image)
#         return classes 

st.title("SaferNet with AI")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:

        u_img = Image.open(uploaded_file)
        st.image(u_img, caption='Uploaded Image', use_column_width=True)

        st.write("")

        if st.button('predict'):
                st.write("Result...")
                loaded_model = get_model()
                image = np.asarray(u_img)/255
                my_image= resize(image, (224,224)).reshape((1, 224*224*3)).T
                start = time.time()
                label = loaded_model.predict(my_image)
                end = time.time()
                # label = label.item()
                print(label)
                st.write(end - start)

                # res = sign_names.get(label)
                st.markdown(label)
                
    
    
