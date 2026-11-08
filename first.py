
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# Display Function
def display():

    # Clear screen
    glClear(GL_COLOR_BUFFER_BIT)

    # Set white color
    glColor3f(1.0, 1.0, 1.0)

    # ==============================
    # 1. TRAPEZOID
    # ==============================

    glBegin(GL_QUADS)

    glVertex3f(0.05, 0.05, 0.0)
    glVertex3f(0.35, 0.05, 0.0)
    glVertex3f(0.40, 0.35, 0.0)
    glVertex3f(0.00, 0.35, 0.0)

    glEnd()


    # ==============================
    # 2. PENTAGON-LIKE SHAPE
    # ==============================

    glBegin(GL_TRIANGLES)

    # Triangle 1 - Red
    glColor3f(1.0, 0.0, 0.0)

    glVertex3f(0.5, 0.05, 0.0)
    glVertex3f(0.75, 0.05, 0.0)
    glVertex3f(0.5, 0.35, 0.0)


    # Triangle 2 - Magenta
    glColor3f(1.0, 0.0, 1.0)

    glVertex3f(0.5, 0.35, 0.0)
    glVertex3f(0.75, 0.05, 0.0)
    glVertex3f(0.75, 0.35, 0.0)


    # Triangle 3 - Cyan
    glColor3f(0.0, 1.0, 1.0)

    glVertex3f(0.5, 0.35, 0.0)
    glVertex3f(0.75, 0.35, 0.0)
    glVertex3f(0.63, 0.50, 0.0)


    # ==============================
    # 3. TRIANGLE
    # ==============================

    glColor3f(1.0, 1.0, 1.0)

    glVertex3f(0.30, 0.65, 0.0)
    glVertex3f(0.60, 0.65, 0.0)
    glVertex3f(0.45, 0.85, 0.0)

    glEnd()

    # Execute OpenGL commands
    glFlush()


# Initialization Function
def init():

    # Background color: Black
    glClearColor(0.0, 0.0, 0.0, 0.0)

    # Projection settings
    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    glOrtho(0.0, 1.0, 0.0, 1.0, -10.0, 10.0)


# Main Function
def main():

    # Initialize GLUT
    glutInit()

    # Display mode
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    # Window size
    glutInitWindowSize(600, 600)

    # Window position
    glutInitWindowPosition(100, 100)

    # Create window
    glutCreateWindow(b"Basic Shapes")

    # Initialize settings
    init()

    # Register display function
    glutDisplayFunc(display)

    # Start main loop
    glutMainLoop()


# Run program
if __name__ == "__main__":
    main()
