
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

angle = 0.0


def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.53, 0.81, 0.98, 1.0)


def draw_cube(x, y, z, sx, sy, sz, color):
    glPushMatrix()

    glTranslatef(x, y, z)
    glScalef(sx, sy, sz)

    glColor3f(*color)
    glutSolidCube(1)

    glPopMatrix()


def draw_roof():
    glColor3f(0.55, 0.12, 0.08)

    # Front triangular roof
    glBegin(GL_TRIANGLES)

    glVertex3f(-1.2, 1.0, 1.1)
    glVertex3f(1.2, 1.0, 1.1)
    glVertex3f(0.0, 2.0, 1.1)

    # Back triangular roof
    glVertex3f(-1.2, 1.0, -1.1)
    glVertex3f(1.2, 1.0, -1.1)
    glVertex3f(0.0, 2.0, -1.1)

    glEnd()

    # Roof slopes
    glColor3f(0.7, 0.15, 0.1)

    glBegin(GL_QUADS)

    # Left roof slope
    glVertex3f(-1.2, 1.0, 1.1)
    glVertex3f(0.0, 2.0, 1.1)
    glVertex3f(0.0, 2.0, -1.1)
    glVertex3f(-1.2, 1.0, -1.1)

    # Right roof slope
    glVertex3f(0.0, 2.0, 1.1)
    glVertex3f(1.2, 1.0, 1.1)
    glVertex3f(1.2, 1.0, -1.1)
    glVertex3f(0.0, 2.0, -1.1)

    glEnd()


def draw_house():

    # Main house body
    draw_cube(0, 0, 0, 2.4, 2.0, 2.2,
              (1.0, 0.85, 0.55))

    # Roof
    draw_roof()

    # Door
    draw_cube(0, -0.45, 1.115, 0.55, 1.1, 0.08,
              (0.35, 0.15, 0.05))

    # Door handle
    glPushMatrix()
    glColor3f(1.0, 0.85, 0.0)
    glTranslatef(0.18, -0.45, 1.17)
    glutSolidSphere(0.045, 20, 20)
    glPopMatrix()

    # Left window
    draw_cube(-0.75, 0.35, 1.12, 0.45, 0.45, 0.06,
              (0.1, 0.65, 1.0))

    # Right window
    draw_cube(0.75, 0.35, 1.12, 0.45, 0.45, 0.06,
              (0.1, 0.65, 1.0))

    # Window frames
    glColor3f(1.0, 1.0, 1.0)

    for x in [-0.75, 0.75]:
        glBegin(GL_LINES)

        glVertex3f(x - 0.225, 0.35, 1.16)
        glVertex3f(x + 0.225, 0.35, 1.16)

        glVertex3f(x, 0.125, 1.16)
        glVertex3f(x, 0.575, 1.16)

        glEnd()

    # Chimney
    draw_cube(0.65, 1.65, -0.3, 0.3, 1.0, 0.3,
              (0.6, 0.2, 0.1))


def draw_ground():

    glColor3f(0.15, 0.65, 0.15)

    glBegin(GL_QUADS)

    glVertex3f(-10, -1.02, -10)
    glVertex3f(10, -1.02, -10)
    glVertex3f(10, -1.02, 10)
    glVertex3f(-10, -1.02, 10)

    glEnd()


def display():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Camera
    glTranslatef(0, 0, -7)
    glRotatef(20, 1, 0, 0)
    glRotatef(angle, 0, 1, 0)

    draw_ground()
    draw_house()

    glutSwapBuffers()


def update(value):
    global angle

    angle += 1

    if angle >= 360:
        angle = 0

    glutPostRedisplay()
    glutTimerFunc(25, update, 0)


def reshape(w, h):

    if h == 0:
        h = 1

    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(45, w / h, 1, 100)

    glMatrixMode(GL_MODELVIEW)


def main():

    glutInit(sys.argv)

    glutInitDisplayMode(
        GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH
    )

    glutInitWindowSize(800, 600)
    glutCreateWindow(b"3D House Design - Python OpenGL")

    init()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glutTimerFunc(25, update, 0)

    glutMainLoop()


if __name__ == "__main__":
    main()
