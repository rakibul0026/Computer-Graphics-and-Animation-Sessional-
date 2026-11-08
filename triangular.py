from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,0,0)
    
    glBegin(GL_TRIANGLES)
    glVertex2f(2,1)
    glVertex2f(6,1)
    glVertex2f(4,5)
    
    glEnd()
    glFlush()
def init():
    #clearcolor, matrixmode(projection/modelview), loadidentity, ortho, glutInit,  glutInitDisplayMode,glutMainLoop,windowSize, windowPosition, createWindow, displayFunc
    glClearColor(0,0,0,0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,10,0,10,-1,1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    
    
    
    
def main():

if__name__=="__main__":
    main()
    

    