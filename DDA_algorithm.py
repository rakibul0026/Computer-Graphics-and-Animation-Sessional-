
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# DDA Line Drawing Algorithm
def DDA(x1, y1, x2, y2):

    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    if steps == 0:
        glBegin(GL_POINTS)
        glVertex2i(round(x1), round(y1))
        glEnd()
        return

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    glBegin(GL_POINTS)

    for i in range(steps + 1):
        glVertex2i(round(x), round(y))

        x += x_inc
        y += y_inc

    glEnd()


# Display function
def display():

    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)
    glPointSize(5)

    # Draw line using DDA
    DDA(100, 100, 500, 350)

    glFlush()


# Initialize
def init():

    glClearColor(1, 1, 1, 1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(0, 600, 0, 600)


# Main function
def main():

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)

    glutCreateWindow(b"DDA Line Drawing Algorithm")

    init()

    glutDisplayFunc(display)

    glutMainLoop()


if __name__ == "__main__":
    main()
