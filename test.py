import streamlit as st
import cv2
import numpy as np
import time
import streamlit.components.v1 as components

# Streamlit setup
st.title("Virtual Keyboard with Hand Tracking")

# Display an HTML component asking for camera permission
components.html("""
    <script type="text/javascript">
        // Request camera permission using the browser API
        async function requestCameraAccess() {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ video: true });
                console.log("Camera access granted");
            } catch (error) {
                alert("Camera access denied. Please allow access to the camera.");
                console.log("Camera access denied:", error);
            }
        }
        requestCameraAccess();  // Call the function to request permission
    </script>
    <h3 style="color: red;">Please allow camera access in your browser for the app to work properly.</h3>
    <p>Once you grant permission, the application will start the camera feed for hand tracking.</p>
""", height=150)

st.title("Live Camera Feed")

# Add a message asking for camera access
st.write("Please click 'Start Camera' to allow access to your webcam.")

# Button to trigger camera access
start_camera = st.button("Start Camera")

# Initialize the video capture object
cap = None

if start_camera:
    # Ask for permission to access the camera
    st.write("Trying to access the camera... Please allow access when prompted.")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        st.error("Error: Could not open video capture. Please ensure your browser allows camera access.")
        st.stop()

    # Display placeholder for the captured image
    image_placeholder = st.empty()

    # Application loop to display the camera feed
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Error: Frame not captured.")
            break

        # Flip the frame horizontally for a mirror effect
        frame = cv2.flip(frame, 1)

        # Convert the frame to RGB (Streamlit uses RGB, OpenCV uses BGR)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Update the image on the Streamlit page
        image_placeholder.image(rgb_frame)

    # Release resources after the loop
    cap.release()
    cv2.destroyAllWindows()