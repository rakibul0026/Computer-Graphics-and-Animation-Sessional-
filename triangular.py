from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    
    glBegin(GL_TRIANGLES)
    glVertex2f(2,1)
    glVertex2f(6,1)
    glVertex2f(4,5)
    
    glEnd()
    glFlush()
def init():
    glClearColor(1,1,1,1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,10,0,10,-1,1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    
    glutCreateWindow(b"Triangular")
    
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__=="__main__":
    main()
    

    
