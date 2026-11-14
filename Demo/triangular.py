
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def display():
    # Clear all pixels
    glClear(GL_COLOR_BUFFER_BIT)

    # Set white color
    glColor3f(1.0, 1.0, 1.0)

    # ==============================
    # 1. Trapezoid
    # ==============================
    glBegin(GL_QUADS)

    glVertex3f(0.05, 0.05, 0.0)
    glVertex3f(0.35, 0.05, 0.0)
    glVertex3f(0.40, 0.35, 0.0)
    glVertex3f(0.00, 0.35, 0.0)

    glEnd()

    # ==============================
    # 2. Pentagon-like Shape
    # ==============================
    glBegin(GL_TRIANGLES)

    # First triangle - Red
    glColor3f(1.0, 1.0, 0.0)

    glVertex3f(0.5, 0.05, 0.0)
    glVertex3f(0.75, 0.05, 0.0)
    glVertex3f(0.5, 0.35, 0.0)

    # Second triangle - Magenta
    glColor3f(1.0, 0.0, 1.0)

    glVertex3f(0.5, 0.35, 0.0)
    glVertex3f(0.75, 0.05, 0.0)
    glVertex3f(0.75, 0.35, 0.0)

    # Third triangle - Cyan
    glColor3f(0.0, 1.0, 1.0)

    glVertex3f(0.5, 0.35, 0.0)
    glVertex3f(0.75, 0.35, 0.0)
    glVertex3f(0.63, 0.50, 0.0)

    # ==============================
    # 3. Triangle
    # ==============================

    glVertex3f(0.30, 0.65, 0.0)
    glVertex3f(0.60, 0.65, 0.0)
    glVertex3f(0.45, 0.85, 0.0)

    glEnd()

    # Execute OpenGL commands
    glFlush()


def init():

    # Background color - Black
    glClearColor(0.0, 0.0, 0.0, 0.0)

    # Projection settings
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glOrtho(0.0, 1.0, 0.0, 1.0, -10.0, 10.0)


def main():

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)

    glutCreateWindow(b"OpenGL Shapes")

    init()

    glutDisplayFunc(display)

    glutMainLoop()


if __name__ == "__main__":
    main()
