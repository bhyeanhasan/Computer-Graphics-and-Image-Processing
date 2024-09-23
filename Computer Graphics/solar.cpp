#include <graphics.h>
#include <math.h>
#include <conio.h>

// Define constants for the screen size and planet orbits
#define SCREEN_WIDTH 800
#define SCREEN_HEIGHT 600
#define SUN_RADIUS 30

// Function to draw a planet orbiting around the sun
void drawPlanet(int centerX, int centerY, int orbitRadius, int planetRadius, float angle, int color) {
    // Calculate the planet's position based on the orbit and angle
    int x = centerX + orbitRadius * cos(angle);
    int y = centerY + orbitRadius * sin(angle);

    // Draw the planet at the calculated position
    setcolor(color);
    setfillstyle(SOLID_FILL, color);
    fillellipse(x, y, planetRadius, planetRadius);
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Center of the solar system (Sun's position)
    int centerX = SCREEN_WIDTH / 2;
    int centerY = SCREEN_HEIGHT / 2;

    // Initial angles for each planet
    float mercuryAngle = 0, venusAngle = 0, earthAngle = 0, marsAngle = 0;

    // Simulation loop
    while (!kbhit()) {
        cleardevice(); // Clear the screen

        // Draw the Sun
        setcolor(YELLOW);
        setfillstyle(SOLID_FILL, YELLOW);
        fillellipse(centerX, centerY, SUN_RADIUS, SUN_RADIUS);

        // Draw Mercury
        drawPlanet(centerX, centerY, 50, 5, mercuryAngle, LIGHTGRAY);
        mercuryAngle += 0.04; // Increment Mercury's angle

        // Draw Venus
        drawPlanet(centerX, centerY, 80, 8, venusAngle, LIGHTCYAN);
        venusAngle += 0.03; // Increment Venus's angle

        // Draw Earth
        drawPlanet(centerX, centerY, 110, 10, earthAngle, BLUE);
        earthAngle += 0.02; // Increment Earth's angle

        // Draw Mars
        drawPlanet(centerX, centerY, 140, 7, marsAngle, RED);
        marsAngle += 0.015; // Increment Mars's angle

        delay(20); // Delay to control the speed of the animation
    }

    closegraph(); // Close the graphics mode
    return 0;
}
