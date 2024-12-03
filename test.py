import cv2
import streamlit as st

# Streamlit setup
st.title("Real-Time Video Capture")

# Password input to control access
password = st.text_input("Enter Password to Start Video", type="password")
correct_password = "1234"  # Set your desired password here

if password == correct_password:
    # Start video capture
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Error: Could not open video capture.")
        st.stop()

    # Placeholder for displaying the video frames
    frame_placeholder = st.empty()

    st.success("Access Granted! Video is running...")

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Error: Frame not captured.")
            break

        # Flip the frame for mirror view
        frame = cv2.flip(frame, 1)

        # Convert the frame from BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the frame in Streamlit
        frame_placeholder.image(rgb_frame)

    # Release resources when done
    cap.release()

elif password:
    st.error("Access Denied! Incorrect Password.")
