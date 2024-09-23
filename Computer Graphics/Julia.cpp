#include <graphics.h>
#include <complex>
#include <iostream>

// Julia function: determines whether a point belongs to the Julia set
int julia(std::complex<double> z, std::complex<double> c, int max_iter) {
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

    // Julia set settings
    double min_re = -2.0, max_re = 2.0;
    double min_im = -2.0, max_im = 2.0;
    int max_iter = 100;

    // Get user input for the complex constant c
    double real_part, imag_part;
    std::cout << "Enter the real part of the constant c: ";
    std::cin >> real_part;
    std::cout << "Enter the imaginary part of the constant c: ";
    std::cin >> imag_part;

    // Create the complex constant c with user inputs
    std::complex<double> c(real_part, imag_part);

    // Loop over each pixel on the screen
    for (int x = 0; x < width; x++) {
        for (int y = 0; y < height; y++) {
            // Map pixel coordinates to the complex plane
            double re = min_re + (x / (double)width) * (max_re - min_re);
            double im = min_im + (y / (double)height) * (max_im - min_im);
            std::complex<double> z(re, im);

            // Get the iteration count for the Julia function
            int iter = julia(z, c, max_iter);

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
