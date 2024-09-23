#include <graphics.h>
#include <complex>
#include <iostream>

// Mandelbrot function: determines whether a point belongs to the Mandelbrot set
int mandelbrot(std::complex<double> c, int max_iter) {
    std::complex<double> z = 0;
    int iter = 0;
    while (abs(z) <= 2 && iter < max_iter) {
        z = z * z + c;
        iter++;
    }
    return iter;
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Screen dimensions
    int width = getmaxx();
    int height = getmaxy();

    // Mandelbrot settings
    double min_re = -2.5, max_re = 1.5;
    double min_im = -1.5, max_im = 1.5;
    int max_iter = 100;

    // Loop over each pixel on the screen
    for (int x = 0; x < width; x++) {
        for (int y = 0; y < height; y++) {
            // Map pixel coordinates to the complex plane
            double re = min_re + (x / (double)width) * (max_re - min_re);
            double im = min_im + (y / (double)height) * (max_im - min_im);
            std::complex<double> c(re, im);

            // Get the iteration count for the Mandelbrot function
            int iter = mandelbrot(c, max_iter);

            // Map the iteration count to a color
            int color = iter == max_iter ? 0 : iter % 15 + 1;
            putpixel(x, y, color);
        }
    }

    std::cout << "Press any key to exit...";
    getch();
    closegraph();
    return 0;
}
