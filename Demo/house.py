
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def display():

    # Clear screen
    glClear(GL_COLOR_BUFFER_BIT)

    # =================================
    # 1. House Body (Red Rectangle)
    # =================================

    glColor3f(0.85, 0.05, 0.0)

    glBegin(GL_QUADS)

    glVertex2f(45, 55)
    glVertex2f(665, 55)
    glVertex2f(665, 405)
    glVertex2f(45, 405)

    glEnd()

    # =================================
    # 2. Roof (Dark Blue Triangle)
    # =================================

    glColor3f(0.0, 0.12, 0.38)

    glBegin(GL_TRIANGLES)

    glVertex2f(45, 405)
    glVertex2f(355, 585)
    glVertex2f(665, 405)

    glEnd()

    # =================================
    # 3. Door (Green Rectangle)
    # =================================

    glColor3f(0.0, 0.60, 0.30)

    glBegin(GL_QUADS)

    glVertex2f(252, 55)
    glVertex2f(458, 55)
    glVertex2f(458, 315)
    glVertex2f(252, 315)

    glEnd()

    # =================================
    # 4. Left Window
    # =================================

    glColor3f(0.0, 0.60, 0.30)

    glBegin(GL_QUADS)

    glVertex2f(101, 158)
    glVertex2f(198, 158)
    glVertex2f(198, 256)
    glVertex2f(101, 256)

    glEnd()

    # =================================
    # 5. Right Window
    # =================================

    glBegin(GL_QUADS)

    glVertex2f(512, 158)
    glVertex2f(610, 158)
    glVertex2f(610, 256)
    glVertex2f(512, 256)

    glEnd()

    # Display
    glFlush()


def init():

    # White background
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # Set projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(0, 800, 0, 650)


def main():

    glutInit()

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(772, 625)

    glutInitWindowPosition(100, 100)

    glutCreateWindow(b"House Drawing")

    init()

    glutDisplayFunc(display)

    glutMainLoop()


if __name__ == "__main__":
    main()
