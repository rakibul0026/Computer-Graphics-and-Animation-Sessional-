#include <GL/glut.h>
#include <stdlib.h>
#include <math.h>


void rectangle(float x1, float y1, float x2, float y2,
               float r, float g, float b)
{
    glColor3f(r, g, b);
    glBegin(GL_POLYGON);
        glVertex2f(x1, y1);
        glVertex2f(x2, y1);
        glVertex2f(x2, y2);
        glVertex2f(x1, y2);
    glEnd();
}

// Draw Polygon
void polygon(float points[][2], int n,
             float r, float g, float b)
{
    glColor3f(r, g, b);
    glBegin(GL_POLYGON);
    for (int i = 0; i < n; i++)
        glVertex2f(points[i][0], points[i][1]);
    glEnd();
}

// Draw Line
void line(float x1, float y1, float x2, float y2,
          float r, float g, float b, float width)
{
    glColor3f(r, g, b);
    glLineWidth(width);
    glBegin(GL_LINES);
        glVertex2f(x1, y1);
        glVertex2f(x2, y2);
    glEnd();
}

// Draw Circle
void circle(float cx, float cy, float radius,
            float r, float g, float b)
{
    glColor3f(r, g, b);
    glBegin(GL_TRIANGLE_FAN);
        glVertex2f(cx, cy);

        for (int i = 0; i <= 100; i++)
        {
            float angle = 2.0f * 3.1415926f * i / 100;

            glVertex2f(cx + radius * cos(angle),
                       cy + radius * sin(angle));
        }
    glEnd();
}

void window(float x, float y)
{
    rectangle(x, y, x + 35, y + 30, 0, 0, 0);

    rectangle(x + 3, y + 3, x + 32, y + 27,
              1.0f, 0.75f, 0.75f);

    line(x + 17.5f, y + 3, x + 17.5f, y + 27,
         0, 0, 0, 2);

    line(x + 3, y + 15, x + 32, y + 15,
         0, 0, 0, 2);
}

void display()
{
    glClear(GL_COLOR_BUFFER_BIT);
    glLoadIdentity();

    // 1. Sky
    rectangle(0, 0, 640, 480,
              0.48f, 0.75f, 0.92f);

    // 2. Small Sun
    circle(90, 400, 23, 1.0f, 0.85f, 0.0f);

    for (int i = 0; i < 360; i += 45)
    {
        float angle = i * 3.1415926f / 180.0f;

        float x1 = 90 + 27 * cos(angle);
        float y1 = 400 + 27 * sin(angle);

        float x2 = 90 + 39 * cos(angle);
        float y2 = 400 + 39 * sin(angle);

        line(x1, y1, x2, y2,
             1.0f, 0.85f, 0.0f, 2);
    }

    rectangle(0, 100, 640, 200,
              0.0f, 0.35f, 0.0f);

    line(0, 200, 640, 200, 0, 0, 0, 2);

    float side[][2] = {
        {190, 200},
        {245, 200},
        {245, 300},
        {190, 300}
    };

    polygon(side, 4, 1.0f, 0.60f, 0.0f);

    // 5. Front Wall
    rectangle(245, 200, 435, 300,
              1.0f, 0.60f, 0.0f);

    // 6. Roof
    float roof[][2] = {
        {190, 300},
        {215, 340},
        {410, 340},
        {435, 300}
    };

    polygon(roof, 4, 0.72f, 0.22f, 0.12f);

    // 7. House Outlines
    line(190, 200, 190, 300, 0, 0, 0, 3);
    line(190, 300, 215, 340, 0, 0, 0, 3);
    line(215, 340, 410, 340, 0, 0, 0, 3);
    line(410, 340, 435, 300, 0, 0, 0, 3);

    line(190, 300, 245, 300, 0, 0, 0, 3);
    line(245, 200, 245, 300, 0, 0, 0, 3);
    line(215, 340, 245, 300, 0, 0, 0, 3);

    line(435, 300, 435, 200, 0, 0, 0, 3);
    line(245, 200, 435, 200, 0, 0, 0, 3);

    window(270, 250);
    window(370, 250);

    rectangle(320, 200, 355, 255, 0, 0, 0);

    rectangle(323, 203, 352, 252,
              1.0f, 0.72f, 0.72f);

    glutSwapBuffers();
}

void init()
{
    glClearColor(0.48f, 0.75f, 0.92f, 1.0f);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    gluOrtho2D(0, 640, 0, 480);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}

void keyboard(unsigned char key, int x, int y)
{
    if (key == 27  key == 'q'  key == 'Q')
        exit(0);
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(640, 480);
    glutInitWindowPosition(100, 100);

    glutCreateWindow("2D House Drawing");

    init();

    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard);

    glutMainLoop();

    return 0;
}
