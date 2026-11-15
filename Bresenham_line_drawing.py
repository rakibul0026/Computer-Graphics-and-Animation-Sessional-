
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

x1, y1, x2, y2 = 0, 0, 0, 0


def display():

    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.0, 1.0, 0.0)

    glPointSize(2.0)

    glBegin(GL_POINTS)

    dx = x2 - x1
    dy = y2 - y1

    p = (2 * dy) - dx

    i = x1
    j = y1

    while i <= x2 and j <= y2:

        if p >= 0:

            i = i + 1
            j = j + 1

            if i > x2 or j > y2:
                break

            print(f"{i:.2f} {j:.2f}")

            glVertex2f(i / 100, j / 100)

            p = p + (2 * dy) - (2 * dx)

        elif p < 0:

            i = i + 1

            if i > x2 or j > y2:
                break

            print(f"{i:.2f} {j:.2f}")

            glVertex2f(i / 100, j / 100)

            p = p + (2 * dy)

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

    global x1, y1, x2, y2

    print("Enter first point:")
    x1, y1 = map(int, input().split())

    print("Enter second point:")
    x2, y2 = map(int, input().split())

    glutInit()

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(500, 500)

    glutInitWindowPosition(100, 100)

    glutCreateWindow(b"Bresenham Line Drawing Algorithm")

    init()

    glutDisplayFunc(display)

    glutMainLoop()


if __name__ == "__main__":
    main()
