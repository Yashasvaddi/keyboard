import cv2
import streamlit as st

st.title("Camera Access Test")

try:
    for i in range(5):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"Camera found at index {i}")
            break

    cap = cv2.VideoCapture(i)
    if not cap.isOpened():
        st.error("Error: Cannot access the camera. Please check the camera and permissions.")
    else:
        st.success("Camera is accessible.")
        ret, frame = cap.read()
        if ret:
            st.image(frame, channels="BGR")
        else:
            st.error("Error: Unable to capture a frame from the camera.")
    cap.release()
except Exception as e:
    st.error(f"An error occurred: {e}")
