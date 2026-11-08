from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    
    #glBegin(GL_QUADS)
    glBegin(GL_TRIANGLES)
    #glVertex3f(1,5,0.0)
     #glVertex3f(5,5,0.0)
    #glVertex3f(7,1,0.0)
    #glVertex3f(0,1,0.0)
    
    glVertex2f(2, 1)
    glVertex2f(6, 1)
    glVertex2f(4, 5)
    glEnd()
    
    glFlush()
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1,8,0,7,-10,10)
    glMatrixMode(GL_MODELVIEW)
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Trapezoid")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
    
if __name__=="__main__":
    main()