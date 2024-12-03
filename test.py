import cv2
import streamlit as st

def main():
    st.title("Live Camera Feed")
   
    camera = cv2.VideoCapture(0)

    # Check if the webcam is accessible
    if not camera.isOpened():
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Camera Permission</title>
</head>
<body>
    <h1>Camera Permission Example</h1>
    <button id="start-camera">Request Camera Access</button>
    <video id="video" autoplay playsinline style="display: none;"></video>
    <script>
        const startCameraButton = document.getElementById('start-camera');
        const videoElement = document.getElementById('video');

        startCameraButton.addEventListener('click', async () => {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ video: true });
                videoElement.srcObject = stream;
                videoElement.style.display = 'block';
                alert('Camera access granted!');
            } catch (error) {
                alert('Camera access denied or not available.');
                console.error('Error accessing camera:', error);
            }
        });
    </script>
</body>
</html>
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
