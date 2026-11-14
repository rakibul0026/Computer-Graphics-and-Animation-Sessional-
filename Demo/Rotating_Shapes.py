from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,1.0)
    
    glBegin(GL_TRIANGLES)
    glVertex3f(2.0,2.0,0.0)
    glVertex3f(8.0,2.0,0.0)
    glVertex3f(4.0,8.0,0.0)
    glEnd()
    glFlush()
    
def init():
    glClearColor(0.0,0.0,0.0,1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,10,0,10,-1,1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
def main():
    
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"Triangle")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
   
    
    
if __name__=="__main__":
    main()
