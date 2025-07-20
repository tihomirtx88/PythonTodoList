import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

# Camera input
with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")

# File uploader input
uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

# Convert and display grayscale image
def convert_and_display(image, source):
    img = Image.open(image)
    gray_img = img.convert('L')
    st.image(gray_img, caption=f"Grayscale Image from {source}")

# Process camera input
if camera_image:
    convert_and_display(camera_image, "Camera")

# Process uploaded file
if uploaded_image:
    convert_and_display(uploaded_image, "Upload")