
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def display():

    glClear(GL_COLOR_BUFFER_BIT)

    # Main roof (Gray)
    glBegin(GL_QUADS)
    glColor3f(0.30, 0.39, 0.48)
    glVertex2f(223, 506)
    glVertex2f(668, 506)
    glVertex2f(779, 356)
    glVertex2f(334, 356)
    glEnd()

    # Main house body (Dark Blue)
    glBegin(GL_QUADS)
    glColor3f(0.09, 0.19, 0.29)
    glVertex2f(334, 100)
    glVertex2f(779, 100)
    glVertex2f(779, 356)
    glVertex2f(334, 356)
    glEnd()

    # Left house body (Dark Teal)
    glBegin(GL_QUADS)
    glColor3f(0.08, 0.30, 0.29)
    glVertex2f(112, 100)
    glVertex2f(334, 100)
    glVertex2f(334, 356)
    glVertex2f(112, 356)
    glEnd()

    # Left triangular roof (Purple)
    glBegin(GL_TRIANGLES)
    glColor3f(0.62, 0.0, 0.85)
    glVertex2f(112, 356)
    glVertex2f(334, 356)
    glVertex2f(223, 506)
    glEnd()

    # Door
    glBegin(GL_QUADS)
    glColor3f(0.48, 0.19, 0.37)
    glVertex2f(168, 100)
    glVertex2f(279, 100)
    glVertex2f(279, 250)
    glVertex2f(168, 250)
    glEnd()

    # Left Window
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.38, 0.0)
    glVertex2f(368, 230)
    glVertex2f(501, 230)
    glVertex2f(501, 320)
    glVertex2f(368, 320)
    glEnd()

    # Left Window - Vertical bar
    glBegin(GL_QUADS)
    glColor3f(0.65, 0.25, 0.55)
    glVertex2f(430, 230)
    glVertex2f(438, 230)
    glVertex2f(438, 320)
    glVertex2f(430, 320)
    glEnd()

    # Left Window - Horizontal bar
    glBegin(GL_QUADS)
    glColor3f(0.65, 0.25, 0.55)
    glVertex2f(368, 269)
    glVertex2f(501, 269)
    glVertex2f(501, 277)
    glVertex2f(368, 277)
    glEnd()

    # Right Window
    glBegin(GL_QUADS)
    glColor3f(0.20, 0.40, 0.32)
    glVertex2f(590, 230)
    glVertex2f(723, 230)
    glVertex2f(723, 320)
    glVertex2f(590, 320)
    glEnd()

    # Right Window - Vertical bar
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.65, 0.45)
    glVertex2f(654, 230)
    glVertex2f(660, 230)
    glVertex2f(660, 320)
    glVertex2f(654, 320)
    glEnd()

    # Right Window - Horizontal bar
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.65, 0.45)
    glVertex2f(590, 273)
    glVertex2f(723, 273)
    glVertex2f(723, 279)
    glVertex2f(590, 279)
    glEnd()

    glFlush()


def init():

    # Background color - Green
    glClearColor(0.16, 0.60, 0.0, 1.0)

    # Projection settings
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(0, 1000, 0, 600)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(1000, 600)
    glutInitWindowPosition(100, 100)

    glutCreateWindow(b"House Design")

    init()

    glutDisplayFunc(display)

    glutMainLoop()


if __name__ == "__main__":
    main()
