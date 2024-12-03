import cv2
import streamlit as st

def main():
    st.title("Live Camera Feed")

    camera1 = cv2.VideoCapture(0)  # Try other indices if needed
    if not camera1.isOpened():
        st.error("Unable to access the camera.")
    else:
        st.error("Camera is accessible.")
        camera1.release()
    # Access the webcam
    camera = cv2.VideoCapture(0)

    # Check if the webcam is accessible
    if not camera.isOpened():
        st.error("Unable to access the webcam.")
        return

    st.write("Click the button below to stop the live feed.")

    # Streamlit container to show the live feed
    camera_feed = st.empty()

    # Button to stop the feed
    stop_feed = st.button("Stop Live Feed")

    while not stop_feed:
        ret, frame = camera.read()
        if not ret:
            st.error("Failed to read frame from webcam.")
            break

        # Convert the frame from BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the live frame
        camera_feed.image(frame_rgb, channels="RGB", use_column_width=True)

    camera.release()
    cv2.destroyAllWindows()
    st.write("Live feed stopped.")

if __name__ == "__main__":
    main()
