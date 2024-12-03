import streamlit as st
import cv2
import numpy as np
import time

# Streamlit setup
st.title("Virtual Keyboard with Hand Tracking")

# Ask for camera permission message
st.markdown("""
    <h3 style="color: red;">Please allow camera access in your browser for the app to work properly.</h3>
    <p>Once you grant permission, the application will start the camera feed for hand tracking.</p>
    """, unsafe_allow_html=True)

# Initialize video capture
cap = cv2.VideoCapture(0)

# Check if the camera is accessible
if not cap.isOpened():
    st.error("Error: Camera not accessible. Please make sure the camera is available and permissions are granted.")
    st.stop()

# Other Streamlit widgets
run_app = st.checkbox("Run Keyboard Application")

# Timer for frame processing
last_capture_time = time.time()
capture_interval = 1.25  # Time interval in seconds

# Display placeholder for the captured image
image_placeholder = st.empty()

# Application loop
while run_app:
    ret, frame = cap.read()
    if not ret:
        st.error("Error: Frame not captured. Make sure camera permissions are granted.")
        break

    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Show the video feed in Streamlit
    image_placeholder.image(framergb, channels="RGB")

    # Process the frame every 1.25 seconds
    current_time = time.time()
    if current_time - last_capture_time >= capture_interval:
        last_capture_time = current_time
        # Add any additional processing here (e.g., hand tracking, keyboard interaction)

# Release the capture when done
cap.release()
cv2.destroyAllWindows()
