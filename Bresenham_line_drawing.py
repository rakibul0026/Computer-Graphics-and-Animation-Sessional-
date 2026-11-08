
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# Window size
WIDTH = 600
HEIGHT = 600


# Bresenham Line Drawing Algorithm
def bresenham(x1, y1, x2, y2):

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Determine direction
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    err = dx - dy

    glBegin(GL_POINTS)

    while True:

        # Draw pixel
        glVertex2i(x1, y1)

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x1 += sx

        if e2 < dx:
            err += dx
            y1 += sy

    glEnd()


# Display Function
def display():

    glClear(GL_COLOR_BUFFER_BIT)

    # Set line color (White)
    glColor3f(1.0, 1.0, 1.0)

    # Draw line from (100, 100) to (400, 300)
    bresenham(100, 100, 400, 300)

    glFlush()


# Initialization Function
def init():

    glClearColor(0.0, 0.0, 0.0, 1.0)

    glColor3f(1.0, 1.0, 1.0)

    glPointSize(3.0)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    gluOrtho2D(0, WIDTH, 0, HEIGHT)


# Main Function
def main():

    glutInit()

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(WIDTH, HEIGHT)

    glutInitWindowPosition(100, 100)

    glutCreateWindow(b"Bresenham Line Drawing Algorithm")

    init()

    glutDisplayFunc(display)

    glutMainLoop()


if __name__ == "__main__":
    main()
