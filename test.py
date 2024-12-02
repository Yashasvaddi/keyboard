import streamlit as st
import numpy as np

def draw_circle(radius):
    x = 0
    y = radius
    d = 3 - 2 * radius
    points = []

    while x <= y:
        # Plot the eight points of the circle using symmetry
        points.extend(get_circle_points(x, y))
        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1

    # Display the circle in a grid format
    display_circle_on_grid(points)

def get_circle_points(x, y):
    # Return points in all octants using symmetry
    return [(x, y), (-x, y), (x, -y), (-x, -y),
            (y, x), (-y, x), (y, -x), (-y, -x)]

def display_circle_on_grid(points):
    # Create a grid (as a numpy array of zeros)
    grid_size = 20  # Define the grid size, large enough to contain the circle
    grid = np.zeros((grid_size, grid_size), dtype=int)

    # Mark the points on the grid
    for (x, y) in points:
        if 0 <= x + grid_size // 2 < grid_size and 0 <= y + grid_size // 2 < grid_size:
            grid[y + grid_size // 2, x + grid_size // 2] = 1  # Mark the point on grid

    # Display the grid
    for row in grid:
        row_str = ''.join(['#' if cell == 1 else '.' for cell in row])
        st.markdown(row_str)

# Example usage:
draw_circle(5)
