import turtle as t
import streamlit as st

# Create a drawing
screen = t.Screen()
t.circle(50)
screen.getcanvas().postscript(file="drawing.eps")

# Convert and display the image
st.image("drawing.eps", caption="Turtle Drawing")
