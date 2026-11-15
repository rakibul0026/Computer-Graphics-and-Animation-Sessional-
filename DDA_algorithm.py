
#(10,10) and (80,60)
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *


def display():

    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)

    glPointSize(2.0)

    glBegin(GL_POINTS)

    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    if steps == 0:
        glVertex2f(x1/100, y1/100)

    else:

        x_inc = dx / steps
        y_inc = dy / steps

        x = float(x1)
        y = float(y1)

        for i in range(steps + 1):

            print(f"{x:.2f}, {y:.2f}")

            glVertex2f(x/100, y/100)

            x = x + x_inc
            y = y + y_inc

    glEnd()

    glFlush()


def init():

    glClearColor(0.0, 0.0, 0.0, 0.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():

    global x1, x2, y1, y2

    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))

    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    glutInit()

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(500, 500)

    glutInitWindowPosition(100, 100)

    glutCreateWindow(b"DDA Line Drawing Algorithm")

    init()

    glutDisplayFunc(display)

    glutMainLoop()


if __name__ == "__main__":
    main()
