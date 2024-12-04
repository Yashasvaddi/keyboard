import speech_recognition as sr
import streamlit as st
import pyttsx3

# Streamlit app title
st.title("Live Captioning")

# Initialize the recognizer
recognizer = sr.Recognizer()
engine = pyttsx3.init()
# Infinite loop to keep listening and updating captions
while True:
    with sr.Microphone() as source:
        st.write("Listening...")
        print("Listening...")
        audio = recognizer.listen(source)
        
        try:
            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio)
            st.write("You said: " + text)
            engine.say("You said: " + text)
            engine.runAndWait()
        
        except sr.UnknownValueError:
            st.write("Could not understand audio")
            print("Could not understand audio")
        
        except sr.RequestError as e:
            st.write(f"Error with the API: {e}")
            print(f"Error with the API: {e}")
        