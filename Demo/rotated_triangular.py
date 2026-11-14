
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Initial angle
_angle = 90.0
_cameraAngle = 0.0


# Initializes 3D rendering
def initRendering():

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)

    # Sky blue background
    glClearColor(0.7, 0.9, 1.0, 1.0)


# Called when window is resized
def handleResize(w, h):

    if h == 0:
        h = 1

    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(45.0, float(w) / float(h), 1.0, 200.0)


# Draws the 3D scene
def drawScene():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glRotatef(-_cameraAngle, 0.0, 1.0, 0.0)
    glTranslatef(0.0, 0.0, -5.0)

    # =================================
    # 1. Rotating Trapezoid
    # =================================

    glPushMatrix()

    glTranslatef(0.0, -1.0, 0.0)

    glRotatef(_angle, 0.0, 0.0, -1.0)

    glBegin(GL_QUADS)

    glColor3f(1.0, 0.0, 0.0)

    glVertex3f(-0.7, -0.5, 0.0)
    glVertex3f(0.7, -0.5, 0.0)
    glVertex3f(0.7, 0.5, 0.0)
    glVertex3f(-0.7, 0.5, 0.0)

    glEnd()

    glPopMatrix()

    # =================================
    # 2. Rotating Pentagon-like Shape
    # =================================

    glPushMatrix()

    glTranslatef(1.0, 1.0, 0.0)

    glRotatef(_angle, 0.0, 1.0, 0.0)

    glScalef(0.7, 0.7, 0.7)

    glBegin(GL_TRIANGLES)

    glColor3f(0.0, 1.0, 0.0)

    # First triangle
    glVertex3f(-0.5, -0.5, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glVertex3f(-0.5, 0.0, 0.0)

    # Second triangle
    glVertex3f(-0.5, 0.0, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glVertex3f(0.5, 0.0, 0.0)

    # Third triangle
    glVertex3f(-0.5, 0.0, 0.0)
    glVertex3f(0.5, 0.0, 0.0)
    glVertex3f(0.0, 0.5, 0.0)

    glEnd()

    glPopMatrix()

    # =================================
    # 3. Rotating Triangle
    # =================================

    glPushMatrix()

    glTranslatef(-1.0, 1.0, 0.0)

    glRotatef(_angle, 1.0, 0.0, 0.0)

    glBegin(GL_TRIANGLES)

    glColor3f(0.0, 0.0, 1.0)

    glVertex3f(0.5, -0.5, 0.0)
    glVertex3f(0.0, 0.5, 0.0)
    glVertex3f(-0.5, -0.5, 0.0)

    glEnd()

    glPopMatrix()

    # Swap buffers
    glutSwapBuffers()


# Updates rotation angle
def update(value):

    global _angle

    _angle += 2.0

    if _angle > 360:
        _angle -= 360

    # Refresh the scene
    glutPostRedisplay()

    # Call update again after 25 milliseconds
    glutTimerFunc(25, update, 0)


# Main function
def main():

    glutInit()

    glutInitDisplayMode(
        GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH
    )

    glutInitWindowSize(400, 400)

    glutCreateWindow(b"Rotating Shapes")

    initRendering()

    # Register callback functions
    glutDisplayFunc(drawScene)

    glutReshapeFunc(handleResize)

    glutTimerFunc(25, update, 0)

    glutMainLoop()


if __name__ == "__main__":
    main()
